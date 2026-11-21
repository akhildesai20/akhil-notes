#!/usr/bin/env python3
"""Rebuild Akhil Notes from the owner's final variable TTF. No external outlines.
Run: python build.py /path/to/AkhilsNotes-Variable.ttf --out build
Requires fonttools; Pillow is optional (proof sheets).
"""
import argparse, copy, math, json, unicodedata as ud, logging, itertools, os, re
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.varLib import build as varbuild
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.ttLib.tables._g_l_y_f import (
    Glyph, GlyphCoordinates, GlyphComponent,
    OVERLAP_COMPOUND, MORE_COMPONENTS, ARGS_ARE_XY_VALUES, ROUND_XY_TO_GRID,
    ARG_1_AND_2_ARE_WORDS, WE_HAVE_A_SCALE, WE_HAVE_AN_X_AND_Y_SCALE, WE_HAVE_A_TWO_BY_TWO,
)
from fontTools.ttLib.tables._f_v_a_r import NamedInstance
from fontTools.otlLib.builder import buildStatTable
from fontTools.feaLib.builder import addOpenTypeFeaturesFromString
from fontTools.misc.roundTools import otRound
from fontTools.agl import UV2AGL
from array import array
logging.basicConfig(level=logging.ERROR)
REPO_URL='' 
CORE='ªºÆæŒœÐðÞþØøĐđĦħŁłẞßȘșȚțıȷ'+''.join(map(chr,[0x300,0x301,0x302,0x303,0x304,0x306,0x307,0x308,0x30A,0x30B,0x30C,0x326,0x327,0x328]))+'¨¯´¸ˆˇ˘˙˛˜˝¡«»¿‚„‹›§¶'
PLUS='‖⟨⟩¦¬µ฿†‡₡₦₨₩₪₫₭₮₱₲₴₵₸₺₼₽₾₿ℓ№Ω℮↖↗↘↙∂∅∏∫Ⓓ▪▫▴▵▸▹▾▿◂◃'
VIET='ƠơƯưẠạẢảẤấẦầẨẩẪẫẬậẮắẰằẲẳẴẵẶặẸẹẺẻẾếỀềỂểỄễỆệỈỉỊịỌọỎỏỐốỒồỔổỖỗỘộỚớỜờỞởỠỡỢợỤụỦủỨứỪừỬửỮữỰựỴỵỶỷ'+ '\u0309\u031b\u0323'
WEIGHTS=[(400,'Regular'),(500,'Medium'),(600,'SemiBold'),(700,'Bold'),(800,'ExtraBold'),(900,'Black')]
MARKS={0x300:'gravecomb',0x301:'acutecomb',0x302:'circumflexcomb',0x303:'tildecomb',0x304:'macroncomb',0x306:'brevecomb',0x307:'dotaccentcomb',0x308:'dieresiscomb',0x309:'hookabovecomb',0x30a:'ringcomb',0x30b:'hungarumlautcomb',0x30c:'caroncomb',0x31b:'horncomb',0x323:'dotbelowcomb',0x326:'commabelowcomb',0x327:'cedillacomb',0x328:'ogonekcomb'}
BELOW={0x323,0x326,0x327,0x328}
DIGITS=['zero','one','two','three','four','five','six','seven','eight','nine']
SUPERIORS='⁰¹²³⁴⁵⁶⁷⁸⁹'
SUBSCRIPTS='₀₁₂₃₄₅₆₇₈₉'
# Release figures rebuilt so small digits keep the same stem weight as full digits.
REBUILD_FIGURES=set([0x00B2,0x00B3,0x00B9,0x2070,*range(0x2074,0x207A),*range(0x2080,0x208A),0x00BC,0x00BD,0x00BE,*range(0x2150,0x215F)])
VULGAR_FRACTIONS=((0x00BC,(1,),(4,)),(0x00BD,(1,),(2,)),(0x00BE,(3,),(4,)),(0x2150,(1,),(7,)),(0x2151,(1,),(9,)),(0x2152,(1,),(1,0)),(0x2153,(1,),(3,)),(0x2154,(2,),(3,)),(0x2155,(1,),(5,)),(0x2156,(2,),(5,)),(0x2157,(3,),(5,)),(0x2158,(4,),(5,)),(0x2159,(1,),(6,)),(0x215A,(5,),(6,)),(0x215B,(1,),(8,)),(0x215C,(3,),(8,)),(0x215D,(5,),(8,)),(0x215E,(7,),(8,)))
FIGURE_SCALE=0.7
# Standard ligatures (liga, on by default). Longest first for OpenType matching.
LIGA_SEQS=('ffi','ffl','ff','fi','fl')
# Discretionary joins (dlig): doubles, classic digraphs, high-value English pairs.
DLIG_SEQS=(
    'tt','ll','oo','ee','ss','pp','rr','nn','mm','cc','dd','gg','bb','zz','aa','ii','uu',
    'st','ct','th','ch','ck','qu','sp','sk','ly','ng','wh','sh','ph','gh','he','in','er',
    'io','le','hi','ic','li','an','at','as',
)
# Per-pair spacing overrides (lowercase key). pull is added between advances (negative = tighter).
LIGA_LOOSE=set('sp sk ck ch ll oo pp nn mm cc dd ii he in io le hi ic li sh ph gh ly'.split())
LIGA_TIGHT=set('at as'.split())
# Milder than default digraph — was cramped when pulled tight/double.
LIGA_EASED=set('an uu ng'.split())
# Trigraph with mixed spacing: looser i–n, eased n–g (ng was too tight).
LIGA_MIXED=(('ing',('loose','eased')),)
CORE_OFFICIAL='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzªºÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿĀāĂăĄąĆćĊċČčĎďĐđĒēĖėĘęĚěĞğĠġĢģĦħĪīĮįİıĶķĹĺĻļĽľŁłŃńŅņŇňŐőŒœŔŕŘřŚśŞşŠšŤťŪūŮůŰűŲųŴŵŶŷŸŹźŻżŽžȘșȚțȷẀẁẂẃẄẅẞỲỳ'+''.join(chr(c) for c in MARKS if c not in (0x309,0x31b,0x323))+'`¨¯´¸ˆˇ˘˙˚˛˜˝0123456789!\"#\'()*+,-./:;?[]\\_{}¡«·»¿–—‘’‚“”„•…‹› \u00a0$%&<=>@^|~¢£¥§©®°¶×÷€™−'

def polygon(points): return [(float(x),float(y),1) for x,y in points]
def contour_area(contour):
    pts=[(x,y) for x,y,_ in contour]
    return sum(pts[i][0]*pts[(i+1)%len(pts)][1]-pts[(i+1)%len(pts)][0]*pts[i][1] for i in range(len(pts)))/2
def as_outer(contour):
    # Match provenance letter outers: positive area fills ink; negative cuts a hole.
    return contour if contour_area(contour)>=0 else contour[::-1]
def as_counter(contour):
    return contour if contour_area(contour)<0 else contour[::-1]
def stroke(points,width):
    # Fixed topology: round caps and mitered joins with bounded miter length.
    # Orientation matches letter outers so layered bars add ink instead of punching holes.
    p=[complex(x,y) for x,y in points]; r=width/2
    dirs=[(b-a)/abs(b-a) for a,b in zip(p,p[1:])]; norms=[v*1j for v in dirs]
    edge=[]
    for sign in [1,-1]:
        side=[]
        for i,q in enumerate(p):
            if i==0: v=norms[0]
            elif i==len(p)-1: v=norms[-1]
            else:
                z=norms[i-1]+norms[i]; v=z/max(abs(z),0.0001); v/=max(0.55, (v*norms[i].conjugate()).real)
            side.append(q+sign*r*v)
        edge.append(side)
    cap1=[p[-1]+r*dirs[-1]*complex(math.cos(math.pi/2-k*math.pi/8),math.sin(math.pi/2-k*math.pi/8)) for k in range(1,8)]
    cap0=[p[0]+r*dirs[0]*complex(math.cos(-math.pi/2-k*math.pi/8),math.sin(-math.pi/2-k*math.pi/8)) for k in range(1,8)]
    return as_outer(polygon([(z.real,z.imag) for z in edge[0]+cap1+edge[1][::-1]+cap0]))
def bounds(cs):
    pts=[(x,y) for c in cs for x,y,_ in c]; return (min(x for x,y in pts),min(y for x,y in pts),max(x for x,y in pts),max(y for x,y in pts)) if pts else (0,0,0,0)
def transform(cs, a=1,b=0,c=0,d=1,tx=0,ty=0):
    out=[[(a*x+c*y+tx,b*x+d*y+ty,f) for x,y,f in q] for q in cs]
    return [q[::-1] for q in out] if a*d-b*c<0 else out
def move(cs,x=0,y=0):return transform(cs,tx=x,ty=y)
def align(cs,x=None,y=None,center=False):
    l,b,r,t=bounds(cs); return move(cs,0 if x is None else x-((l+r)/2 if center else l),0 if y is None else y-b)
def circle(x,y,r,n=24):return as_outer(polygon([(x+r*math.cos(-2*math.pi*i/n),y+r*math.sin(-2*math.pi*i/n)) for i in range(n)]))
def ring(x,y,r,w):return [as_outer(circle(x,y,r+w/2)),as_counter(circle(x,y,max(5,r-w/2)))]
def thicken(cs, delta):
    """Expand ink by delta along normals. Same point/contour count — VF safe."""
    if delta<=0: return cs
    out=[]
    for contour in cs:
        pts=list(contour); n=len(pts)
        if n<3:
            out.append(contour); continue
        area=contour_area(pts)
        # Positive outers expand outward; negative counters shrink (more ink).
        sense=1 if area>=0 else -1
        grown=[]
        for i in range(n):
            x0,y0,_=pts[i-1]; x1,y1,f=pts[i]; x2,y2,_=pts[(i+1)%n]
            e1x,e1y=x1-x0,y1-y0; e2x,e2y=x2-x1,y2-y1
            # Right-hand normal of each edge, averaged at the vertex.
            nx=e1y+e2y; ny=-(e1x+e2x)
            length=math.hypot(nx,ny) or 1.0
            grown.append((x1+sense*delta*nx/length,y1+sense*delta*ny/length,f))
        out.append(grown)
    return out
def optical_scale(cs, scale, grow):
    """Scale outlines, then thicken so stems stay near full digit weight."""
    return thicken(transform(cs,a=scale,d=scale),grow)
def arc(cx,cy,rx,ry,start,end,n=15):return [(cx+rx*math.cos(math.radians(start+(end-start)*i/(n-1))),cy+ry*math.sin(math.radians(start+(end-start)*i/(n-1)))) for i in range(n)]
def cubic_points(start, segments, n=9):
    result=[start];prev=start
    for b,c,d in segments:
        a=prev
        for j in range(1,n+1):
            t=j/n;u=1-t;result.append(tuple(u*u*u*a[k]+3*u*u*t*b[k]+3*u*t*t*c[k]+t*t*t*d[k] for k in (0,1)))
        prev=d
    return result

def glyph(cs):
    g=Glyph(); g.numberOfContours=len(cs); coords=[]; flags=[]; ends=[]
    for q in cs:
        coords.extend((otRound(x),otRound(y)) for x,y,f in q); flags.extend(f&1 for x,y,f in q); ends.append(len(coords)-1)
    g.coordinates=GlyphCoordinates(coords);g.flags=array('B',flags);g.endPtsOfContours=ends
    from fontTools.ttLib.tables.ttProgram import Program
    g.program=Program();g.program.fromBytecode([])
    # Flags must advertise overlap for constructed unions in TrueType.
    if flags: g.flags[0]|=0x40
    return g

def rename_digits(f):
    m={str(i):n for i,n in enumerate(DIGITS)}; g=f['glyf']; order=f.getGlyphOrder();g.glyphs={m.get(n,n):v for n,v in g.glyphs.items()};
    for v in g.glyphs.values():
        if v.isComposite():
            for c in v.components:c.glyphName=m.get(c.glyphName,c.glyphName)
    f['hmtx'].metrics={m.get(n,n):v for n,v in f['hmtx'].metrics.items()}
    for t in f['cmap'].tables:
        if t.isUnicode():t.cmap={cp:m.get(n,n) for cp,n in t.cmap.items()}
    f.setGlyphOrder([m.get(n,n) for n in order]); g.glyphOrder=f.getGlyphOrder(); f['post'].mapping={}; f['post'].extraNames=[]

class Master:
 def __init__(self,f,weight,slant):
    self.f=f; self.g=f['glyf']; self.cmap=dict(f.getBestCmap());self.orig=dict(self.cmap); self.weight=weight;self.slant=slant;self.shear=math.tan(math.radians(-slant)); self.width=24+46*(weight-400)/500;self.new={};self.anchors={};self.modified=set(); self.source={}
    for n in f.getGlyphOrder():
        g=self.g[n];coords,ends,flags=g.getCoordinates(self.g); q=[];start=0
        for end in ends:
            q.append([(float(coords[i][0]),float(coords[i][1]),flags[i]&1) for i in range(start,end+1)]);start=end+1
        self.source[n]=q
 def get(self,ch):
    n=self.cmap.get(ord(ch),ch) if len(ch)==1 else ch
    if n in self.new and self.new[n]:
        return copy.deepcopy(self.new[n])
    if n in self.g.glyphs and self.g[n].isComposite():
        return self.decompose(n)
    return copy.deepcopy(self.new.get(n,self.source.get(n,[])))
 def decompose(self,name):
    """Decompose a composite to contour tuples for bounds / further builds."""
    from fontTools.pens.basePen import BasePen
    from fontTools.pens.transformPen import TransformPen
    class Collector(BasePen):
        def __init__(self, glyphSet):
            super().__init__(glyphSet); self.contours=[]; self._cur=None
        def _moveTo(self,pt): self._cur=[(float(pt[0]),float(pt[1]),1)]
        def _lineTo(self,pt): self._cur.append((float(pt[0]),float(pt[1]),1))
        def _curveToOne(self,p1,p2,p3): self._cur.append((float(p3[0]),float(p3[1]),1))
        def _qCurveToOne(self,p1,p2): self._cur.append((float(p2[0]),float(p2[1]),1))
        def _closePath(self):
            if self._cur and len(self._cur)>2: self.contours.append(self._cur)
            self._cur=None
        def _endPath(self): self._closePath()
        def addComponent(self,glyphName,transformation,**kwargs):
            t=TransformPen(self,transformation)
            self.glyphSet[glyphName].draw(t,self.glyphSet)
    pen=Collector(self.g); self.g[name].draw(pen,self.g); return pen.contours
 def upright(self,ch):
    return transform(self.get(ch),c=-self.shear)
 def make(self,cp,cs,advance=None,mark=False,already_slanted=False,name=None,keep_advance=False):
    n=name or self.cmap.get(cp) or (UV2AGL.get(cp) if cp is not None else None) or (f'uni{cp:04X}' if cp is not None else None)
    if n in self.source:self.modified.add(n)
    if not already_slanted: cs=transform(cs,c=self.shear)
    l,b,r,t=bounds(cs)
    if mark: advance=0
    elif advance is None:
        advance=otRound(r-l+80);cs=move(cs,34-l);l=34
    if keep_advance and n in self.f['hmtx'].metrics:advance=self.f['hmtx'][n][0]
    self.new[n]=cs; self.g.glyphs[n]=glyph(cs);self.f['hmtx'][n]=(otRound(advance),otRound(l) if cs else 0)
    if n not in self.f.getGlyphOrder():self.f.setGlyphOrder(self.f.getGlyphOrder()+[n]);self.g.glyphOrder=self.f.getGlyphOrder()
    if cp is not None:self.cmap[cp]=n
    return n
 def gname(self,ch):
    return self.cmap[ord(ch)] if len(ch)==1 else ch
 def component_place(self,ch,x=None,y=None,center_x=False,center_y=False,scale_x=1.0,scale_y=1.0):
    """Place an existing master glyph as a TrueType component (already slanted)."""
    # TrueType 2.14 component scales must stay under 2.
    scale_x=float(min(1.999,max(0.05,scale_x))); scale_y=float(min(1.999,max(0.05,scale_y)))
    name=self.gname(ch)
    raw=copy.deepcopy(self.new.get(name,self.source.get(name,[])))
    l0,b0,r0,t0=bounds(raw)
    tx=0 if x is None else x-(scale_x*((l0+r0)/2 if center_x else l0))
    ty=0 if y is None else y-(scale_y*((b0+t0)/2 if center_y else b0))
    return (name,(scale_x,0.0,0.0,scale_y,float(tx),float(ty)))
 def make_composite(self,cp,parts,advance=None,name=None):
    """Layer existing glyphs. OVERLAP_COMPOUND keeps intersections solid in browsers."""
    n=name or self.cmap.get(cp) or (UV2AGL.get(cp) if cp is not None else None) or (f'uni{cp:04X}' if cp is not None else None)
    if n in self.source:self.modified.add(n)
    g=Glyph(); g.numberOfContours=-1; g.components=[]
    for i,(gname,xf) in enumerate(parts):
        xx,xy,yx,yy,dx,dy=xf
        c=GlyphComponent(); c.glyphName=gname; c.x=int(otRound(dx)); c.y=int(otRound(dy))
        flags=ARGS_ARE_XY_VALUES|ROUND_XY_TO_GRID
        if abs(c.x)>127 or abs(c.y)>127: flags|=ARG_1_AND_2_ARE_WORDS
        if abs(xx-1)>1e-6 or abs(yy-1)>1e-6 or abs(xy)>1e-6 or abs(yx)>1e-6:
            if abs(xy)<=1e-6 and abs(yx)<=1e-6 and abs(xx-yy)<=1e-6:
                flags|=WE_HAVE_A_SCALE; c.transform=[[xx,0],[0,xx]]
            elif abs(xy)<=1e-6 and abs(yx)<=1e-6:
                flags|=WE_HAVE_AN_X_AND_Y_SCALE; c.transform=[[xx,0],[0,yy]]
            else:
                flags|=WE_HAVE_A_TWO_BY_TWO; c.transform=[[xx,xy],[yx,yy]]
        if i<len(parts)-1: flags|=MORE_COMPONENTS
        if i==0: flags|=OVERLAP_COMPOUND
        c.flags=flags; g.components.append(c)
    self.g.glyphs[n]=g
    try:
        from fontTools.pens.boundsPen import BoundsPen
        bp=BoundsPen(self.g); g.draw(bp,self.g); l,b,r,t=bp.bounds if bp.bounds else (0,0,0,0)
    except Exception:
        l,b,r,t=0,0,0,0
    if advance is None:
        advance=otRound(max(r+34,self.f['hmtx'].metrics.get(parts[0][0],(r+80,0))[0]))
    self.new[n]=self.decompose(n)
    self.f['hmtx'][n]=(otRound(advance),otRound(l) if r>l else 0)
    if n not in self.f.getGlyphOrder():self.f.setGlyphOrder(self.f.getGlyphOrder()+[n]);self.g.glyphOrder=self.f.getGlyphOrder()
    if cp is not None:self.cmap[cp]=n
    return n
 def line(self,*pts):return [stroke(pts,self.width)]
 def curve(self,start,*segments):return self.line(*cubic_points(start,segments))
 def get_at(self,ch,x,y,center=False,scale=1):return align(transform(self.upright(ch),a=scale,d=scale),x,y,center)
 def place_glyph(self,ch,x=None,y=None,center_x=False,center_y=False,scale_x=1,scale_y=1):
    cs=transform(self.upright(ch),a=scale_x,d=scale_y); l,b,r,t=bounds(cs)
    dx=0 if x is None else x-((l+r)/2 if center_x else l)
    dy=0 if y is None else y-((b+t)/2 if center_y else b)
    return move(cs,dx,dy)
 def ensure_tick(self):
    """Short vertical stem for bitcoin-like ticks; no component scale (keeps VF composites)."""
    if '_tick' not in self.g.glyphs:
        # Same topology at every master: a short stem at natural stroke width.
        self.make(None,self.line((0,0),(0,180)),80,name='_tick')
    return '_tick'
 def stem_components(self,base_ch,x=None,pad=70,count=1,spread=110):
    # Translate-only components (no scale) so ufo2ft keeps them as composites in the VF.
    cs=self.get(base_ch); l,b,r,t=bounds(cs); mid=(l+r)/2; mid_y=(b+t)/2
    xs=[mid if x is None else x] if count<=1 else [((mid if x is None else x)-spread/2),((mid if x is None else x)+spread/2)]
    return [self.component_place('l',x=cx,y=mid_y,center_x=True,center_y=True) for cx in xs]
 def bar_components(self,base_ch,y=None,pad=35,count=1,spread=130):
    cs=self.get(base_ch); l,b,r,t=bounds(cs); mid=(b+t)/2
    ys=[mid if y is None else y] if count<=1 else [((mid if y is None else y)-spread/2),((mid if y is None else y)+spread/2)]
    # Translate-only endash (no scale) so composites survive into the VF.
    return [self.component_place('\u2013',x=(l+r)/2,y=cy,center_x=True,center_y=True) for cy in ys]
 def slash_component(self,base_ch,pad=20):
    cs=self.get(base_ch); l,b,r,t=bounds(cs)
    return [self.component_place('/',x=(l+r)/2,y=(b+t)/2,center_x=True,center_y=True)]
 def join_letters(self,left,right,overlap=None):
    """Fuse two upright letters so they share a spine; stroke weight stays the originals'."""
    a=self.upright(left); b=self.upright(right)
    la,ba,ra,ta=bounds(a); lb,bb,rb,tb=bounds(b)
    if overlap is None:
        # Share about one stem / bowl wall — handwriting digraph, not two loose letters.
        overlap=otRound(self.width*4.5+95)
    joined=a+move(b,ra-lb-overlap,0)
    aw_l=self.f['hmtx'][self.gname(left)][0]; aw_r=self.f['hmtx'][self.gname(right)][0]
    advance=otRound(aw_l+aw_r-overlap)
    return joined, max(advance,otRound(bounds(joined)[2]+40))
 def small_figure(self,digit_name):
    grow=max(2.0,self.width*(1.0-FIGURE_SCALE)*0.5)
    return optical_scale(self.upright(digit_name),FIGURE_SCALE,grow)
 def build_marks(self):
    w=self.width; L=self.line; C=self.curve
    acute=L((-36,0),(44,80)); grave=L((-44,80),(36,0)); circum=L((-105,0),(0,77),(105,0)); caron=L((-105,77),(0,0),(105,77)); breve=C((-102,65),((-83,-18),(68,-38),(102,65))); tilde=C((-105,0),((-50,110),(40,-52),(105,50))); macron=L((-112,4),(112,4)); dot=[circle(0,0,w*.72)]; dia=move(dot,-70)+move(dot,70); ringmark=ring(0,0,65,w); hung=move(acute,-75)+move(acute,75); comma=C((15,0),((13,-45),(-10,-65),(-42,-93))); ced=C((0,0),((34,-40),(29,-70),(-25,-88)),((-45,-103),(-74,-96),(-83,-87))); og=C((0,0),((-38,-50),(-45,-115),(41,-109))); hook=C((-48,66),((-39,128),(73,110),(42,58)),((32,32),(-2,30),(-3,0))); horn=C((0,0),((62,7),(94,45),(88,111))); below=copy.deepcopy(dot)
    marks={0x300:grave,0x301:acute,0x302:circum,0x303:tilde,0x304:macron,0x306:breve,0x307:dot,0x308:dia,0x309:hook,0x30a:ringmark,0x30b:hung,0x30c:caron,0x31b:horn,0x323:below,0x326:comma,0x327:ced,0x328:og}
    for cp,cs in marks.items():
        l,b,r,t=bounds(cs)
        if cp in BELOW:cs=move(cs,-(l+r)/2,-t)
        elif cp!=0x31b:cs=move(cs,-(l+r)/2,-b)
        self.make(cp,cs,0,True,name=MARKS[cp]);marks[cp]=cs
    alt=L((-6,0),(27,52),(1,99));self.make(None,align(alt,0,0,True),0,True,name='caroncomb.alt')
    # Vietnamese stacked marks: place tones alongside the structural mark where possible;
    # this retains clearance without creating excessive line height.
    self.stacks={}
    for base in (0x302,0x306):
        a=marks[base];al,ab,ar,at=bounds(a)
        for tone in (0x300,0x301,0x303,0x309):
            b=marks[tone];bl,bb,br,bt=bounds(b)
            if tone==0x303: b=move(b,0,at+max(18,w*.3)-bb)
            else:
                sign=-1 if tone==0x300 else 1
                b=move(b,sign*(max(abs(al),abs(ar))*.92+max(abs(bl),abs(br))*.78),at*.40-bb)
            n=MARKS[base]+'_'+MARKS[tone]; self.make(None,a+b,0,True,name=n);self.stacks[(base,tone)]=n
    for c,cp in zip('`¨¯´¸ˆˇ˘˙˚˛˜˝',[0x300,0x308,0x304,0x301,0x327,0x302,0x30c,0x306,0x307,0x30a,0x328,0x303,0x30b]):
        if ord(c) in self.orig:continue
        self.make(ord(c),align(marks[cp],34,490 if cp not in BELOW else -100))
 def build_letters(self):
    L=self.line; U=self.upright; C=self.curve
    for ch,base in [('ı','i.dotlessInternal'),('ȷ','j.dotlessInternal')]:self.make(ord(ch),U(base),self.f['hmtx'][base][0])
    # Barred / stroked letters: your letter + endash or slash at natural stroke weight.
    for ch,base in [('Ð','D'),('Đ','D'),('đ','d'),('Ø','O'),('ø','o'),('Ħ','H'),('ħ','h'),('Ł','L'),('ł','l')]:
        cs=self.get(base); l,b,r,t=bounds(cs); mid=(b+t)/2
        base_part=(self.gname(base),(1,0,0,1,0,0))
        aw=self.f['hmtx'][self.gname(base)][0]
        if ch in 'Øø':
            self.make_composite(ord(ch),[base_part]+self.slash_component(base,pad=18),aw)
        elif ch=='Ħ':
            # One en-dash across both stems, upper third — same bar as your handwriting dashes.
            self.make_composite(ord(ch),[base_part,self.component_place('\u2013',x=(l+r)/2,y=t-(t-b)*0.28,center_x=True,center_y=True)],aw)
        elif ch=='ħ':
            self.make_composite(ord(ch),[base_part,self.component_place('\u2013',x=l+otRound((r-l)*0.35),y=t-(t-b)*0.28,center_x=True,center_y=True)],aw)
        elif ch in 'Łł':
            # Diagonal stroke through the stem at self.width (matches every other drawn stroke).
            sx=l+otRound(self.width*0.9); mid_y=(b+t)/2
            diag=L((sx-30,mid_y-110),(sx+otRound((r-l)*0.42)+40,mid_y+110))
            self.make(ord(ch),U(base)+diag)
        elif ch=='đ':
            # Crossbar on the ascender stem, just below the top — like a handwritten d-stroke.
            self.make_composite(ord(ch),[base_part,self.component_place('\u2013',x=r-otRound(self.width*2.2),y=t-otRound((t-b)*0.22),center_x=True,center_y=True)],aw)
        else:
            # Ð Đ: bar through the vertical stem at mid height.
            stem_x=l+otRound(self.width*1.6)
            self.make_composite(ord(ch),[base_part,self.component_place('\u2013',x=stem_x,y=mid,center_x=True,center_y=True)],aw)
    # Digraph capitals/lower: fuse your real letters (same ink, same curves).
    for cp,left,right,overlap in [
        (ord('Æ'),'A','E',otRound(self.width*5.2+130)),
        (ord('Œ'),'O','E',otRound(self.width*4.8+120)),
        (ord('æ'),'a','e',otRound(self.width*4.2+100)),
        (ord('œ'),'o','e',otRound(self.width*4.0+95)),
    ]:
        cs,aw=self.join_letters(left,right,overlap); self.make(cp,cs,aw)
    # Eth: your o + ascending curl at the same stroke width as every drawn mark.
    o=U('o'); ol,ob,orr,ot_=bounds(o)
    curl=C((orr-otRound(self.width*1.2),ot_-20),
           ((orr+30,ot_+90),(orr-40,ot_+190),(orr-170,ot_+230)),
           ((orr-260,ot_+200),(orr-290,ot_+110),(orr-210,ot_+50)))
    self.make(ord('ð'),o+curl)
    # Thorn: your I/l stem + P/p bowl with stems locked to one centerline.
    for ch,stem_ch,bowl_ch in [('Þ','I','P'),('þ','l','p')]:
        stem=U(stem_ch); bowl=U(bowl_ch)
        sl,sb,sr,st=bounds(stem); bl,bb,br,bt=bounds(bowl)
        stem_cx=(sl+sr)/2
        # P/p keep the stem on the left; park that stem on I/l.
        bowl_stem_cx=bl+otRound(self.width*0.95)
        bowl=move(bowl,stem_cx-bowl_stem_cx,0)
        self.make(ord(ch),stem+bowl)
    # Long s: your J flipped vertically then horizontally (dotless j → hook on top, facing in).
    jay=U('ȷ'); jl,jb,jr,jt=bounds(jay)
    longs=transform(jay,a=1,d=-1,ty=jb+jt)          # flip vertical → hook on top
    ll,lb,lr,lt=bounds(longs)
    longs=transform(longs,a=-1,d=1,tx=ll+lr)         # flip horizontal → hook faces the right way
    ll,lb,lr,lt=bounds(longs)
    longs=move(longs,34-ll,-lb); self.make(ord('ſ'),longs,otRound(bounds(longs)[2]+40))
    # Eszett: ſ + s at your stroke weight.
    ss,ss_aw=self.join_letters('ſ','s',otRound(self.width*4.5+110)); self.make(ord('ß'),ss,ss_aw)
    # Capital sharp S: same drawing as ß, optically taller.
    sharp=transform(ss,a=1.12,d=1.18); sl,sb,sr,st=bounds(sharp)
    sharp=move(sharp,34-sl,0); self.make(ord('ẞ'),sharp,otRound(bounds(sharp)[2]+40))
    for ch,base in [('ª','a'),('º','o')]:
        cs=transform(U(base),a=.70,d=.70); cs=align(cs,34,450);self.make(ord(ch),cs+L((34,385),(bounds(cs)[2],385)))
    for ch,base in [('Ơ','O'),('ơ','o'),('Ư','U'),('ư','u')]:
        cs=U(base);l,b,r,t=bounds(cs);self.make(ord(ch),cs+move(U('horncomb'),r-30,t-100))
    # Keep dotless forms independently encoded and preserve dotted i / j.
 def build_punct(self):
    L=self.line;U=self.upright;A=self.get_at
    for ch,base in [('¡','!'),('¿','?')]:
        cs=U(base);l,b,r,t=bounds(cs);self.make(ord(ch),transform(cs,a=-1,d=-1,tx=l+r,ty=t+b))
    for ch,base in [('‹','<'),('›','>'),('«','<'),('»','>')]:
        # Short chevrons use original stroke thickness, not scaled outlines.
        pts=[(190,485),(55,340),(190,195)] if base=='<' else [(55,485),(190,340),(55,195)]
        cs=L(*pts);self.make(ord(ch),cs+(move(cs,175,0) if ch in '«»' else []))
    for ch,base in [('‚','‘'),('„','“')]:self.make(ord(ch),align(U(base),34,-75))
    # Section: horizontally squeezed S with a small zero centered in the middle.
    # make() left-aligns private glyphs; center the zero via composite translate.
    s=transform(U('S'),a=.58,d=1.0)
    z=optical_scale(U('zero'),0.34,self.width*0.42)
    self.make(None,s,name='_Ssection'); self.make(None,z,name='_zerosection')
    sl,sb,sr,st=bounds(self.new['_Ssection']); zl,zb,zr,zt=bounds(self.new['_zerosection'])
    dx=otRound((sl+sr)/2-(zl+zr)/2); dy=otRound((sb+st)/2-(zb+zt)/2)
    self.make_composite(ord('§'),[('_Ssection',(1,0,0,1,0,0)),('_zerosection',(1,0,0,1,dx,dy))],otRound(sr+40))
    self.make(ord('¶'),ring(255,540,145,self.width)+L((286,688),(286,-25))+L((370,688),(370,-25))+L((286,688),(435,688)))
    # Catalog marks for Catalan; uppercase dot slightly higher.
    self.make(None,align(U('·'),34,220),180,name='periodcentered.loclCAT');self.make(None,align(U('·'),34,330),180,name='periodcentered.loclCAT.case')
    self.make(None,U('i'),self.f['hmtx'][self.cmap[ord('i')]][0],name='idotaccent')
 def compose_accents(self,targets):
    # Reconstruct precomposed marks consistently (including old incorrect breve/caron).
    for cp in sorted(targets):
        seq=ud.normalize('NFD',chr(cp));
        if len(seq)<2 or not all(ord(x) in self.cmap for x in seq):continue
        if not all(ord(x) in MARKS for x in seq[1:]):continue
        base=seq[0]; ac=[ord(x) for x in seq[1:]]; base_name=self.cmap[ord(base)]
        if base in 'ij' and any(p not in BELOW and p!=0x31b for p in ac):base_name=self.cmap[ord('ı' if base=='i' else 'ȷ')]
        cs=self.upright(base_name); l,b,r,t=bounds(cs); mid=(l+r)/2; top=t+max(25,self.width*.30); bottom=b-max(18,self.width*.25)
        if 0x31b in ac:
            cs+=move(self.upright('horncomb'),r-30,t-100);ac.remove(0x31b)
        # NFD places below marks before tones; top marks keep linguistic order.
        i=0
        while i<len(ac):
            p=ac[i]; key=(p,ac[i+1]) if i+1<len(ac) else None
            stack=self.stacks.get(key);mk=self.upright(stack or MARKS[p]);ml,mb,mr,mt=bounds(mk);i+=2 if stack else 1
            if p in BELOW:
                cx=(r-45 if p==0x328 else mid); dy=(b+8-mt if p in (0x327,0x328) else bottom-mt);cs+=move(mk,cx-(ml+mr)/2,dy);bottom=min(bottom,mb+dy)-25
            elif p==0x30c and base in 'dltLĽ':
                mk=self.upright('caroncomb.alt');ml,mb,mr,mt=bounds(mk);cs+=move(mk,r+50-ml,t-25-mt)
            else:
                cs+=move(mk,mid-(ml+mr)/2,top-mb);top+=mt-mb+max(22,self.width*.30)
        aw=self.f['hmtx'][self.cmap[ord(base)]][0]
        # preserve original advance where available; widen apostrophe-like carons only.
        if 0x30c in ac and base in 'dltL':aw=max(aw,otRound(bounds(cs)[2]+45))
        # Avoid extreme overhang on narrow accented forms, while leaving normal spacing unchanged.
        cl,cb,cr,ct=bounds(cs);aw=max(aw,otRound(cr+20));
        if cl<0:cs=move(cs,-cl+12,0);aw+=otRound(-cl+12)
        self.make(cp,cs,aw)
 def build_plus(self):
    L=self.line;U=self.upright;A=self.get_at;w=self.width
    # Diagonal arrows: rotations of original vectors (constant stroke width).
    for ch,angle in [('↗',45),('↖',135),('↙',225),('↘',315)]:
        z=math.radians(angle);cs=transform(U('→'),a=math.cos(z),b=math.sin(z),c=-math.sin(z),d=math.cos(z));self.make(ord(ch),align(cs,34,20))
    # Currency / utility as TrueType composites: letter + l / en-dash / slash.
    # ₡ = C + two vertical stems; ₮ = T + two horizontal bars; ₿ = B + two full stems.
    # Use simple bases only — nested components (e.g. đ) fail Fontspector.
    for ch,base,style in [('฿','B','vertical'),('₡','C','doubleStem'),('₦','N','horizontal2'),('₩','W','bars'),('₫','d','under'),('₭','K','kip'),('₮','T','horizontal2'),('₱','P','bars'),('₲','G','vertical'),('₴','S','hryvnia'),('₵','C','vertical'),('₸','T','over'),('₽','P','horizontal'),('₿','B','doubleStem')]:
        base_name=self.gname(base); aw=self.f['hmtx'][base_name][0]
        base_part=(base_name,(1,0,0,1,0,0))
        cs=self.get(base); l,b,r,t=bounds(cs); x=(l+r)/2; y=(b+t)/2
        if style=='vertical': parts=[base_part]+self.stem_components(base,pad=65)
        elif style=='doubleStem':
            # Two full-weight l stems through the letter (baht-like, doubled).
            spread=100 if ch=='₡' else 110
            parts=[base_part]+self.stem_components(base,count=2,spread=spread,pad=55)
        elif style=='diag2':
            s1=self.slash_component(base)[0]; gname,xf=s1
            parts=[base_part,s1,(gname,(xf[0],xf[1],xf[2],xf[3],xf[4]+55,xf[5]))]
        elif style=='horizontal2':
            # Tugrik etc.: two bars through the stem, spaced for bold clarity.
            spread=150 if ch=='₮' else 130
            parts=[base_part]+self.bar_components(base,count=2,spread=spread,pad=35)
        elif style=='horizontal': parts=[base_part]+self.bar_components(base,pad=20)
        elif style=='under': parts=[base_part]+self.bar_components(base,y=b-95,pad=10)
        elif style=='over': parts=[base_part]+self.bar_components(base,y=t+95,pad=10)
        elif style=='slash2':
            s1=self.slash_component(base)[0]; gname,xf=s1
            parts=[base_part,s1,(gname,(xf[0],xf[1],xf[2],xf[3],xf[4],xf[5]+90))]
        elif style=='bars':
            ys=(t-120,t-235) if ch=='₱' else (t-130,t-240)
            pad=20 if ch=='₱' else 25
            parts=[base_part]+self.bar_components(base,y=ys[0],pad=pad)+self.bar_components(base,y=ys[1],pad=pad)
        elif style=='hryvnia':
            parts=[base_part]+self.bar_components(base,y=y-35,pad=35)+self.bar_components(base,y=y+75,pad=35)
        elif style=='kip':
            parts=[base_part,self.component_place('\u2013',x=l+120,y=y,center_x=True,center_y=True)]
        else:
            parts=[base_part]+self.bar_components(base,pad=20)
        self.make_composite(ord(ch),parts,aw)
    # Hand-built currencies at the same stroke width as your letters (self.line / self.curve).
    # Lira: your l stem + open bowl (like a soft C) + two diagonal ticks.
    stem=U('l'); sl,sb,sr,st=bounds(stem)
    sx=(sl+sr)/2
    bowl=self.curve((sx,sb+otRound(self.width)),((sx+220,sb+10),(sx+340,sb+120),(sx+340,sb+280)),((sx+340,sb+400),(sx+220,st-40),(sx+40,st-80)))
    tick1=L((sx-70,sb+420),(sx+160,sb+560)); tick2=L((sx-70,sb+300),(sx+160,sb+440))
    self.make(ord('₺'),stem+bowl+tick1+tick2)
    # Manat: U-like bowl from your curve language + l stem through the middle.
    manat=self.curve((65,8),((65,240),(65,360),(280,360)),((495,360),(495,230),(495,8)))
    self.make(None,manat,name='_manatBase')
    self.make_composite(ord('₼'),[('_manatBase',(1,0,0,1,0,0)),self.component_place('l',x=280,y=(bounds(manat)[1]+bounds(manat)[3])/2,center_x=True,center_y=True)])
    # Lari: open bowl + baseline stroke + two l stems (full weight).
    lari=(self.curve((540,40),((560,-10),(200,-20),(70,180)),((-10,420),(80,700),(360,690)),((520,680),(560,520),(500,300)))
          +L((70,40),(560,40)))
    self.make(None,lari,name='_lariBase')
    ll,lb,lr,lt=bounds(self.get('_lariBase')); cx=(ll+lr)/2; cy=(lb+lt)/2
    self.make_composite(ord('₾'),[
        ('_lariBase',(1,0,0,1,0,0)),
        self.component_place('l',x=cx-55,y=cy,center_x=True,center_y=True),
        self.component_place('l',x=cx+55,y=cy,center_x=True,center_y=True),
    ],otRound(lr+40))
    # Rupee: R + s fused like your digraphs.
    rs,rs_aw=self.join_letters('R','s',otRound(self.width*2.8+40)); self.make(ord('₨'),rs,rs_aw)
    # Shekel: two mirrored handwriting stems with soft tops (same width as l).
    sh1=self.curve((60,30),((60,220),(60,430),(60,620)),((140,620),(300,640),(340,500)),((360,400),(350,220),(350,180)))
    sh2=self.curve((200,450),((200,260),(200,50),(200,30)),((300,30),(480,10),(520,140)),((540,230),(520,420),(520,620)))
    self.make(ord('₪'),sh1+sh2)
    self.make_composite(ord('‖'),[self.component_place('bar',x=60),self.component_place('bar',x=190)])
    self.make(ord('¦'),L((65,-25),(65,295))+L((65,445),(65,775)))
    for ch in '⟨⟩':self.make(ord(ch),L(*([(240,710),(70,340),(240,-20)] if ch=='⟨' else [(70,710),(240,340),(70,-20)])))
    self.make(ord('¬'),L((65,510),(430,510),(430,310)))
    u=self.get('u'); ul,ub,ur,ut=bounds(u)
    # Micro: full l dropped as a descender (translate only — no scale).
    self.make_composite(ord('µ'),[(self.gname('u'),(1,0,0,1,0,0)),self.component_place('l',x=ul+24,y=ub-200,center_x=True)],self.f['hmtx'][self.gname('u')][0])
    self.make(ord('†'),L((210,-25),(210,720))+L((55,480),(365,480)))
    self.make(ord('‡'),L((210,-25),(210,720))+L((55,495),(365,495))+L((55,190),(365,190)))
    self.make(ord('Ω'),L((55,0),(248,0),*arc(365,355,290,330,245,-65),(482,0),(675,0)))
    self.make(ord('∂'),U('o')+L((bounds(U('o'))[2]-30,300),(480,475),(420,630),(260,715),(115,650)))
    self.make_composite(ord('∅'),[(self.gname('O'),(1,0,0,1,0,0))]+self.slash_component('O',pad=25),self.f['hmtx'][self.gname('O')][0])
    self.make(ord('∏'),L((45,685),(685,685))+L((125,685),(125,0))+L((605,685),(605,0)))
    self.make(ord('∫'),L((385,680),(300,725),(235,680),(205,540),(165,150),(125,-140),(65,-215),(-5,-175)))
    self.make(ord('ℓ'),U('l')+L((25,155),(135,320)))
    no=U('N'); nl,nb,nr,nt=bounds(no); small_o=optical_scale(U('o'),0.72,self.width*0.14)
    so=align(small_o,nr+85,420); self.make(ord('№'),no+so+self.place_glyph('hyphen',x=nr+90,y=350,center_y=True,scale_x=1.2))
    self.make(ord('℮'),L(*arc(300,340,230,275,0,323))+L((75,340),(530,340)))
    for ch,base in [('▪','■'),('▫','□'),('▴','▲'),('▵','△'),('▸','▶'),('▹','▷'),('▾','▼'),('▿','▽'),('◂','◀'),('◃','◁')]:
        if ch in '▪▴▸▾◂':cs=transform(U(base),a=.55,d=.55)
        else:
            pts={'▫':[(60,200),(280,200),(280,420),(60,420),(60,200)],'▵':[(55,200),(165,420),(275,200),(55,200)],'▹':[(55,200),(275,310),(55,420),(55,200)],'▿':[(55,420),(165,200),(275,420),(55,420)],'◃':[(275,200),(55,310),(275,420),(275,200)]}[ch];cs=L(*pts)
        self.make(ord(ch),align(cs,34,210))
    # Circled D: ring + reduced D as separate glyphs, composed without transforms.
    self.make(None,ring(410,365,360,w),name='_circleRing')
    d=transform(self.upright('D'),a=.58,d=.58); dl,db,dr,dt=bounds(d)
    self.make(None,move(d,410-(dl+dr)/2,365-(db+dt)/2),name='_Dsmall')
    self.make_composite(ord('Ⓓ'),[('_circleRing',(1,0,0,1,0,0)),('_Dsmall',(1,0,0,1,0,0))])
 def liga_pull(self, kind='default'):
    """Spacing between joined letters. Negative pulls letters together."""
    w=self.width
    if kind=='loose': return -otRound(w*0.35+6)      # more air
    if kind=='eased': return -otRound(w*1.0+14)      # slightly open (an)
    if kind=='tight': return -otRound(w*3.4+58)       # closer
    if kind=='f': return -otRound(w*1.1+18)
    if kind=='double': return -otRound(w*2.4+40)
    return -otRound(w*2.0+32)                         # default digraph
 def liga_pull_for(self, text):
    key=text.lower()
    if key in LIGA_LOOSE: return self.liga_pull('loose')
    if key in LIGA_EASED: return self.liga_pull('eased')
    if key in LIGA_TIGHT: return self.liga_pull('tight')
    if text[0] in 'fF' and len(text)<=3 and all(c in 'filFIL' for c in text):
        return self.liga_pull('f')
    if len(set(key))==1: return self.liga_pull('double')
    return self.liga_pull('default')
 def make_ligature(self, text, pull=None, pulls=None):
    """Pack letters into one glyph with controlled overlap between them."""
    gnames=[self.cmap[ord(ch)] for ch in text]
    out_name='_'.join(gnames)
    if pulls is None:
        gap=self.liga_pull_for(text) if pull is None else pull
        pulls=[gap]*(len(text)-1)
    else:
        pulls=[self.liga_pull(k) if isinstance(k,str) else k for k in pulls]
    out=[]; cursor=0
    for i,gn in enumerate(gnames):
        cs=copy.deepcopy(self.new.get(gn,self.source[gn]))
        adv,lsb=self.f['hmtx'][gn]
        out+=move(cs,cursor-lsb,0)
        if i<len(gnames)-1: cursor+=adv+pulls[i]
        else: cursor+=adv
    l,b,r,t=bounds(out); out=move(out,34-l,0)
    # Keep the pulled advance, remapped to LSB 34.
    advance=otRound(cursor+34-l+max(24,self.width*0.6))
    self.make(None,out,max(advance,otRound(bounds(out)[2]+36)),already_slanted=True,name=out_name)
    return gnames, out_name
 def build_ligatures(self):
    """Create liga/dlig glyphs: lowercase joins plus Title Case (First + lower) pairs."""
    self.liga_subs=[]; self.dlig_subs=[]; seen=set()
    def add(seq, bucket, pulls=None):
        if not seq or any(ord(ch) not in self.cmap for ch in seq): return
        key=''.join(seq)
        if key in seen: return
        seen.add(key)
        gnames, out_name=self.make_ligature(seq, pulls=pulls)
        bucket.append((gnames, out_name))
    for seq in LIGA_SEQS:
        add(seq, self.liga_subs)
        # Title Case form of standard ligatures lives in dlig (Fi, Fl, Ff, Ffi, Ffl).
        add(seq[0].upper()+seq[1:], self.dlig_subs)
    for seq in DLIG_SEQS:
        add(seq, self.dlig_subs)
        add(seq[0].upper()+seq[1:], self.dlig_subs)
    for seq, gaps in LIGA_MIXED:
        add(seq, self.dlig_subs, pulls=gaps)
        add(seq[0].upper()+seq[1:], self.dlig_subs, pulls=gaps)
    # Longest-first so ffi/ing win over shorter pairs.
    self.liga_subs.sort(key=lambda item: (-len(item[0]), item[1]))
    self.dlig_subs.sort(key=lambda item: (-len(item[0]), item[1]))
 def add_features_glyphs(self):
    U=self.upright; L=self.line
    # Fixed tabular advance across all digits at each master; enough room for widest digit.
    aw=max(self.f['hmtx'][n][0] for n in DIGITS)+20
    for n in DIGITS:
        cs=U(n);l,b,r,t=bounds(cs);self.make(None,move(cs,(aw-(r-l))/2-l),aw,name=n+'.tf')
    cs=U('zero'); l,b,r,t=bounds(cs);self.make(None,cs+L((l+120,b+100),(r-120,t-100)),self.f['hmtx']['zero'][0],name='zero.zero')
    self.alts=[]
    for ch in 'a c d e g h l m n o r s t u w y'.split():
        cs=U(ch);l,b,r,t=bounds(cs);cx=(l+r)/2;cy=(b+t)/2
        for i,deg in enumerate((-1.6,1.4),1):
            theta=math.radians(deg);co=math.cos(theta);si=math.sin(theta);alt=transform(cs,a=co,b=si,c=-si,d=co,tx=cx-co*cx+si*cy,ty=cy-si*cx-co*cy+(5 if i==1 else -4))
            self.make(None,alt,self.f['hmtx'][self.cmap[ord(ch)]][0],name=ch+'.alt'+str(i));
        self.alts.append(ch)
    self.build_ligatures()
    # Small figures from full digits: same stem weight, then parked as sups/subs/numr/dnom.
    for i,n in enumerate(DIGITS):
        small=self.small_figure(n); l,b,r,t=bounds(small)
        adv=max(otRound(r-l+48),otRound(self.f['hmtx'][n][0]*FIGURE_SCALE+36))
        body=move(small,34-l,0); _,bb,_,bt=bounds(body)
        sup=move(body,0,810-bt); self.make(ord(SUPERIORS[i]),sup,adv)
        sub=move(body,0,-40-bb); self.make(ord(SUBSCRIPTS[i]),sub,adv)
        numr=move(body,0,580-bt); self.make(None,numr,adv,name=n+'.numr')
        dnom=move(body,0,-5-bb); self.make(None,dnom,adv,name=n+'.dnom')
    for cp,nums,dens in VULGAR_FRACTIONS:
        parts=[]; x=34
        for d in nums:
            g=U(DIGITS[d]+'.numr'); l,b,r,t=bounds(g); parts+=move(g,x-l,0); x+=r-l+6
        slash=U(self.cmap[0x2044]); l,b,r,t=bounds(slash); parts+=move(slash,x-l,0); x+=r-l+4
        for d in dens:
            g=U(DIGITS[d]+'.dnom'); l,b,r,t=bounds(g); parts+=move(g,x-l,0); x+=r-l+6
        self.make(cp,parts,otRound(x+24))
    # Distinct alternate outline for caron on d/l/t. No invented contextual handwriting variants.
    # Set .notdef as a legible box with a diagonal, not a blank.
    if not self.source.get('.notdef'):
        self.make(None,L((50,-100),(50,720),(550,720),(550,-100),(50,-100))+L((70,-80),(530,700)),600,name='.notdef')
    for t in self.f['cmap'].tables:
        if t.isUnicode():t.cmap.update(self.cmap)
    self.f['maxp'].numGlyphs=len(self.f.getGlyphOrder())
 def features(self,kernpairs):
    # Anchor coordinates in master units. Every letter has independent top/bottom anchors.
    f=self.f; out=['languagesystem DFLT dflt;','languagesystem latn dflt;','languagesystem latn CAT;','languagesystem latn TRK;']
    for k in ['top','bottom','horn','caron']:
        for cp,n in MARKS.items():
            kind='bottom' if cp in BELOW else 'horn' if cp==0x31b else 'top'
            if k==kind:out.append(f'markClass {n} <anchor 0 0> @{k};')
    out.append('markClass caroncomb.alt <anchor 0 0> @caron;')
    for n in self.stacks.values():out.append(f'markClass {n} <anchor 0 0> @top;')
    letters=[]
    for cp,n in sorted(self.cmap.items()):
        if not ud.category(chr(cp)).startswith('L') or n in letters:continue
        letters.append(n)
    letters += [ch+'.alt'+str(i) for ch in self.alts for i in (1,2)]+['idotaccent']
    out.append('feature mark {')
    for n in letters:
        l,b,r,t=bounds(self.upright(n)); x=(l+r)/2; top=t+max(25,self.width*.30); bot=b-max(18,self.width*.25);s=self.shear
        # Anchor top above ink plus optical gap; actual marks normalized around zero.
        out.append(f'pos base {n} <anchor {otRound(x+s*top)} {otRound(top)}> mark @top <anchor {otRound(x+s*bot)} {otRound(bot)}> mark @bottom <anchor {otRound(r-30+s*(t-100))} {otRound(t-100)}> mark @horn <anchor {otRound(r+65+s*(t-110))} {otRound(t-110)}> mark @caron;')
    out.append('} mark; feature mkmk {')
    for cp,n in MARKS.items():
        if cp in BELOW or cp==0x31b:continue
        l,b,r,t=bounds(self.upright(n));y=t+max(22,self.width*.30)
        out.append(f'pos mark {n} <anchor {otRound(self.shear*y)} {otRound(y)}> mark @top;')
    out.append('} mkmk;')
    topnames=[n for cp,n in MARKS.items() if cp not in BELOW and cp!=0x31b]+list(self.stacks.values())
    out.append('@AboveMarks = ['+' '.join(topnames)+'];')
    out.append('feature ccmp { '+ ' '.join(f'sub {MARKS[b]} {MARKS[t]} by {n};' for (b,t),n in self.stacks.items())+' sub i\' @AboveMarks by '+self.cmap[ord('ı')]+'; sub j\' @AboveMarks by '+self.cmap[ord('ȷ')]+'; sub [d l t L] caroncomb\' by caroncomb.alt; } ccmp;')
    # Catalan localized middle dot substitutions.
    dot=self.cmap[ord('·')];out.append(f'feature locl {{ script latn; language CAT; sub l {dot}\' l by periodcentered.loclCAT; sub L {dot}\' L by periodcentered.loclCAT.case; language TRK exclude_dflt; sub i by idotaccent; }} locl;')
    out.append('feature tnum { sub ['+' '.join(DIGITS)+'] by ['+' '.join(n+'.tf' for n in DIGITS)+']; } tnum;')
    out.append('feature pnum { sub ['+' '.join(n+'.tf' for n in DIGITS)+'] by ['+' '.join(DIGITS)+']; } pnum;')
    for feat,ending in [('numr','.numr'),('dnom','.dnom')]:out.append('feature '+feat+' { sub ['+' '.join(DIGITS)+'] by ['+' '.join(n+ending for n in DIGITS)+']; } '+feat+';')
    for feat,string in [('sups','⁰¹²³⁴⁵⁶⁷⁸⁹'),('subs','₀₁₂₃₄₅₆₇₈₉')]:out.append('feature '+feat+' { sub ['+' '.join(DIGITS)+'] by ['+' '.join(self.cmap[ord(x)] for x in string)+']; } '+feat+';')
    # Standard contextual fraction feature handles one or multiple digits on either side.
    d='['+' '.join(DIGITS)+']';nm='['+' '.join(n+'.numr' for n in DIGITS)+']';de='['+' '.join(n+'.dnom' for n in DIGITS)+']';slash=self.cmap[ord('/')];fs=self.cmap[ord('⁄')]
    out.append(f'lookup NumSub {{ sub {d} by {nm}; }} NumSub; lookup DenSub {{ sub {d} by {de}; }} DenSub;')
    out.append(f'feature frac {{ sub {d} {slash}\' {d} by {fs}; sub {d}\' lookup NumSub {fs}; sub {d}\' lookup NumSub {nm}; sub {fs} {d}\' lookup DenSub; sub {de} {d}\' lookup DenSub; }} frac;')
    out.append('feature zero { sub zero by zero.zero; } zero;')
    # Standard ligatures (on by default) and discretionary joins including Title Case pairs.
    liga=getattr(self,'liga_subs',[])
    dlig=getattr(self,'dlig_subs',[])
    if liga:
        out.append('feature liga { '+ ' '.join(f"sub {' '.join(src)} by {dst};" for src,dst in liga)+' } liga;')
    if dlig:
        out.append('feature dlig { '+ ' '.join(f"sub {' '.join(src)} by {dst};" for src,dst in dlig)+' } dlig;')
    # Alternates based on rigid rotations of owner vectors; only repeated letters auto-substitute.
    out.append('feature calt { '+ ' '.join(f'sub {c} {c}\' by {c}.alt1; sub {c}.alt1 {c}\' by {c}.alt2;' for c in self.alts)+' } calt;')
    out.append('feature salt { '+ ' '.join(f'sub {c} from [{c}.alt1 {c}.alt2];' for c in self.alts)+' } salt;')
    out.append('feature kern {')
    for a,b,value in kernpairs:out.append(f'pos {a} {b} {value};')
    out.append('} kern;')
    return '\n'.join(out)+'\n'

def kern_plan(masters):
    # Use scanline bounds from actual outlines, choose conservative values across masters.
    # Quadratic off-curve controls are conservatively included as polygon segments.
    names=[masters[0].cmap[ord(c)] for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.,:;!?()[]\"\'’‘“”–—-']
    ys=list(range(-360,801,16)); profiles=[]
    for m in masters:
        prof={}
        for n in names:
            cs=m.get(n);rows=[]
            for y in ys:
                xs=[]
                for q in cs:
                    for a,b in zip(q,q[1:]+q[:1]):
                        if (a[1]<=y<b[1]) or (b[1]<=y<a[1]):xs.append(a[0]+(b[0]-a[0])*(y-a[1])/(b[1]-a[1]))
                rows.append((min(xs),max(xs)) if xs else None)
            prof[n]=(m.f['hmtx'][n][0],rows)
        profiles.append(prof)
    pairs=[]
    for a,b in itertools.product(names,repeat=2):
        if a==b:continue
        values=[];valid=True
        for m,p in zip(masters,profiles):
            aw,A=p[a];_,B=p[b]; gaps=sorted(aw+q[0]-r[1] for r,q in zip(A,B) if r and q)
            if len(gaps)<4:valid=False;break
            # Preserve actual positive clearance at thick/slanted extremes, no forced tightening.
            optical=gaps[int((len(gaps)-1)*.25)];min_gap=gaps[0];target=60 if m.weight==400 else 45
            v=max(-75,min(60,target-optical));v=max(v,20-min_gap);values.append(v)
        if not valid:continue
        if all(x< -12 for x in values):value=int(math.ceil(max(values)/5)*5)
        elif max(values)>12 and min(values)>-20:value=int(math.ceil(max(values)/5)*5)
        else:continue
        if abs(value)>=15:pairs.append((a,b,value))
    return pairs

def names(f,style='Regular',variable=True,italic=False,weight=400):
    t=f['name'];t.names=[];family='Akhil Notes'; compact='AkhilNotes'; ps=compact+'-'+style.replace(' ','');
    d={0:f'Copyright 2026 The Akhil Notes Project Authors ({REPO_URL or "Akhil Desai"})',1:family,2:style,3:'2.000;NONE;'+ps,4:family+' '+style,5:'Version 2.000',6:ps,8:'Akhil Desai',9:'Akhil Desai',10:'A personal handwriting typeface designed by Akhil Desai for everyday notes and digital writing.',11:'https://www.instagram.com/akhilius_',12:'https://www.instagram.com/akhilius_',13:'This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org',14:'https://openfontlicense.org',16:family,17:style}
    if variable:d[25]=compact+('Italic' if italic else '')
    # Legacy style links: only Regular/Italic/Bold/Bold Italic under primary family.
    if not variable and weight not in (400,700):
        label=dict(WEIGHTS)[weight];d[1]=family+' '+label;d[2]='Italic' if italic else 'Regular'
    for i,s in d.items():t.setName(s,i,3,1,0x409)
    f['head'].fontRevision=2.0; f['OS/2'].fsType=0;f['OS/2'].usWeightClass=weight
    sel=f['OS/2'].fsSelection;sel&=~((1<<0)|(1<<5)|(1<<6)|(1<<9));sel|=1<<7
    if italic:sel|=1
    if weight==700:sel|=1<<5
    if weight==400 and not italic:sel|=1<<6
    f['OS/2'].fsSelection=sel;f['head'].macStyle=(1 if weight==700 else 0)|(2 if italic else 0);f['post'].italicAngle=-15 if italic else 0

def finalize_metrics(masters):
    # All styles share bounding-safe vertical metrics: retain original generous line height if accents require it.
    ymin=0;ymax=0
    for m in masters:
        for n in m.f.getGlyphOrder():
            l,b,r,t=bounds(m.get(n));ymin=min(ymin,b);ymax=max(ymax,t)
    winasc=int(math.ceil(ymax));windesc=int(math.ceil(-ymin))
    # Typo/Hhea preserve a practical line rhythm, Win covers every glyph.
    # The owner's long descenders and tall capitals require slightly more than 130% UPM.
    asc=max(950,max(otRound(bounds(m.get(m.cmap[0x1EAE]))[3]) for m in masters)+10);desc=-430
    for m in masters:
        f=m.f;f['OS/2'].version=max(4,f['OS/2'].version);f['OS/2'].sTypoAscender=asc;f['OS/2'].sTypoDescender=desc;f['OS/2'].sTypoLineGap=0;f['OS/2'].usWinAscent=winasc;f['OS/2'].usWinDescent=windesc;f['hhea'].ascent=asc;f['hhea'].descent=desc;f['hhea'].lineGap=0;f['OS/2'].recalcUnicodeRanges(f);f['OS/2'].recalcAvgCharWidth(f)
    return asc,desc

def make_stat(f,italic=False,combined=False):
    axes=[dict(tag='wght',name='Weight',ordering=0,values=[dict(value=w,name=s,**({'flags':2,'linkedValue':700} if w==400 else {})) for w,s in WEIGHTS])]
    if combined:axes.append(dict(tag='slnt',name='Slant',ordering=1,values=[dict(value=0,name='Upright',flags=2,linkedValue=-15),dict(value=-15,name='Italic')]))
    else:axes.append(dict(tag='ital',name='Italic',ordering=1,values=[dict(value=int(italic),name='Italic' if italic else 'Roman',**({} if italic else {'flags':2,'linkedValue':1}))]))
    buildStatTable(f,axes,elidedFallbackName='Regular')

def var_names(f,italic=False,combined=False):
    names(f,'Italic' if italic else 'Regular',True,italic); f['fvar'].instances=[]
    for w,style in WEIGHTS:
        for sl in ([0,-15] if combined else ([-15] if italic else [0])):
            s=style+(' Italic' if sl else '');s='Italic' if s=='Regular Italic' else s
            inst=NamedInstance();inst.subfamilyNameID=f['name'].addName(s,platforms=[(3,1,0x409)]);inst.postscriptNameID=f['name'].addName('AkhilNotes-'+s.replace(' ',''),platforms=[(3,1,0x409)]);inst.coordinates={'wght':w};
            if combined:inst.coordinates['slnt']=sl
            f['fvar'].instances.append(inst)
    for a in f['fvar'].axes:a.axisNameID=f['name'].addName({'wght':'Weight','slnt':'Slant'}[a.axisTag],platforms=[(3,1,0x409)])
    make_stat(f,italic,combined)

def main():
    ap=argparse.ArgumentParser();ap.add_argument('source');ap.add_argument('--out',default='build');ap.add_argument('--repo-url',default='');args=ap.parse_args();global REPO_URL;REPO_URL=args.repo_url;out=Path(args.out);out.mkdir(parents=True,exist_ok=True);(out/'masters').mkdir(exist_ok=True);(out/'fonts').mkdir(exist_ok=True)
    src=TTFont(args.source);assert len(src.getBestCmap())==491 and set(a.axisTag for a in src['fvar'].axes)=={'wght','slnt'},'Use the final 491-character two-axis release.'
    initial=dict(src.getBestCmap()); masters=[]
    for w,s in [(400,0),(900,0),(400,-15),(900,-15)]:
        print('Constructing master',w,s,flush=True);f=instantiateVariableFont(src,{'wght':w,'slnt':s},inplace=False);rename_digits(f)
        if 'STAT' in f:del f['STAT']
        m=Master(f,w,s);m.build_marks();m.build_letters();m.build_punct();m.compose_accents(set(initial)|set(map(ord,CORE+VIET)));m.build_plus();m.add_features_glyphs();masters.append(m)
    print('Computing optical kerning',flush=True);pairs=kern_plan(masters);asc,desc=finalize_metrics(masters)
    ds=DesignSpaceDocument();
    for tag,name,lo,default,hi in [('wght','Weight',400,400,900),('slnt','Slant',-15,0,0)]:a=AxisDescriptor();a.tag=tag;a.name=name;a.minimum=lo;a.default=default;a.maximum=hi;ds.addAxis(a)
    for m in masters:
        f=m.f; style=dict(WEIGHTS)[m.weight]+(' Italic' if m.slant else '');style='Italic' if style=='Regular Italic' else style;names(f,style,False,bool(m.slant),m.weight)
        fea=m.features(pairs); (out/'masters'/f'{m.weight}_{m.slant}.fea').write_text(fea,encoding='utf-8');addOpenTypeFeaturesFromString(f,fea)
        p=out/'masters'/f'{m.weight}_{m.slant}.ttf';f.save(p);sd=SourceDescriptor();sd.path=str(p.resolve());sd.name=p.stem;sd.location={'Weight':m.weight,'Slant':m.slant};ds.addSource(sd)
    ds.write(out/'AkhilNotes.designspace');print('Building variable font',flush=True);var,_,_=varbuild(ds);var_names(var,combined=True);var.save(out/'fonts'/'AkhilNotes[slnt,wght].ttf')
    for sl,filename in [(0,'AkhilNotes[wght].ttf'),(-15,'AkhilNotes-Italic[wght].ttf')]:
        f=instantiateVariableFont(TTFont(out/'fonts'/'AkhilNotes[slnt,wght].ttf'),{'slnt':sl},inplace=False);var_names(f,bool(sl));f.save(out/'fonts'/filename)
    for w,label in WEIGHTS:
        for sl in [0,-15]:
            f=instantiateVariableFont(TTFont(out/'fonts'/'AkhilNotes[slnt,wght].ttf'),{'wght':w,'slnt':sl},inplace=False);style=label+(' Italic' if sl else '');style='Italic' if style=='Regular Italic' else style;names(f,style,False,bool(sl),w);make_stat(f,bool(sl));f.save(out/'fonts'/('AkhilNotes-'+style.replace(' ','')+'.ttf'))
    cmap=var.getBestCmap();report={'source_mapped':len(initial),'mapped':len(cmap),'glyphs':len(var.getGlyphOrder()),'added':len(set(cmap)-set(initial)),'original_mappings_lost':[hex(x) for x in set(initial)-set(cmap)],'core_missing':[f'U+{ord(c):04X}' for c in sorted(set(CORE_OFFICIAL)) if ord(c) not in cmap],'core_previous_gap_missing':[f'U+{ord(c):04X}' for c in CORE if ord(c) not in cmap],'plus_previous_gap_missing':[f'U+{ord(c):04X}' for c in PLUS if ord(c) not in cmap],'vietnamese_previous_gap_missing':[f'U+{ord(c):04X}' for c in VIET if ord(c) not in cmap],'kerning_pairs':len(pairs),'metrics':[asc,desc],'modified_existing_glyphs':len(masters[0].modified),'tables':list(var.keys()),'named_instances':len(var['fvar'].instances),'new_codepoints':[f'U+{cp:04X} {chr(cp)} {ud.name(chr(cp),"UNKNOWN")}' for cp in sorted(set(cmap)-set(initial))]}
    (out/'report.json').write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding='utf-8');print(json.dumps({k:v for k,v in report.items() if k!='new_codepoints'},indent=2,ensure_ascii=True),flush=True)
if __name__=='__main__':main()
