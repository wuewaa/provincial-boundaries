#!/usr/bin/env python
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
from matplotlib.font_manager import fontManager
from scipy import stats
import numpy as np
import matplotlib.patches as mpatches
from cartopy.mpl.ticker import LatitudeFormatter, LongitudeFormatter
fontManager.addfont(r'C:\Windows\Fonts\simkai.ttf')
fname = fontManager.ttflist[-1].name
fontManager.addfont(r'C:\Windows\Fonts\times.ttf')
fnamE = fontManager.ttflist[-1].name

if __name__=='__main__':
    lzn = '沈阳市、大连市、鞍山市、抚顺市、本溪市、'
    lzn +='营口市、辽阳市、铁岭市、盘锦市'
    lzn = lzn.split('、')
    jjj = '北京、天津、安阳、定州、辛集、保定、唐山、廊坊、'
    jjj +='石家庄、秦皇岛、张家口、承德、沧州、衡水、邢台、邯郸'
    jjj = jjj.split('、')
    jjj = [x+'市' for x in jjj]
    sdb = '济南、青岛、烟台、淄博、威海、潍坊、东营、日照、'
    sdb = sdb.split('、')
    sdb = [x+'市' for x in sdb]
    csj = '上海、南京、无锡、常州、苏州、南通、盐城、扬州、镇江、泰州、'
    csj += '杭州、宁波、嘉兴、湖州、绍兴、金华、舟山、台州、'
    csj += '合肥、芜湖、马鞍山、铜陵、安庆、滁州、池州、宣城'
    csj = csj.split('、')
    csj = [x+'市' for x in csj]
    zsj = '广州、深圳、佛山、东莞、中山、珠海、惠州、江门、肇庆、'
    zsj = zsj.split('、')
    zsj = [x+'市' for x in zsj]
    yma = '潮州、梅州、漳州、莆田、宁德、揭阳、汕尾、'
    yma += '福州、厦门、泉州、汕头、温州'
    yma = yma.split('、')
    yma = [x+'市' for x in yma] 
    bbw = '南宁市、北海市、钦州市、防城港市、玉林市、崇左市、'
    bbw += '湛江市、茂名市、阳江市、'
    bbw += '海口市、儋州市、东方市、澄迈县、临高县、昌江黎族自治县'
    bbw = bbw.split('、')

    fig = plt.figure()
    ax = fig.add_subplot(1,1,1,projection=ccrs.PlateCarree())
    pth = r'F:\Linux\bourndarys_china\china-shapefiles\shapefiles\china_country.shp'
    shpsc = shpreader.Reader(pth)
    ax.add_geometries(shpsc.geometries(),ccrs.PlateCarree(),
                      facecolor='none',
                      edgecolor='k',linewidth=0.5)
    pth = r'F:\Linux\bourndarys_china\china-shapefiles\shapefiles\china.shp'
    shpss = shpreader.Reader(pth)
    ax.add_geometries(shpss.geometries(),ccrs.PlateCarree(),
                      facecolor='none',
                      edgecolor='grey',linewidth=0.5)

    pth = r'F:\Linux\bourndarys_china\2022市矢量.shp'
    shps = shpreader.Reader(pth)
    pth = r'F:\Linux\bourndarys_china\2022县矢量.shp'
    shps1 = shpreader.Reader(pth)

    cl = 'k'
    L = []
    cs =  ['辽中南','京津冀','山东半岛','长三角',
            '珠三角','粤闽浙','北部湾']
    k = np.zeros(7)
    for x in list(shps.records())+list(shps1.records()):
        name = x.attributes['地名']
        if name in lzn:
            ax.add_geometries(iter([x.geometry]),ccrs.PlateCarree(),
                      facecolor='b',
                      edgecolor=cl,linewidth=0.5)
            if k[0]==0:
                tmpl = mpatches.Rectangle((0, 0), 1, 1, facecolor='b',
                        label=cs[0])
                L.append(tmpl)
                k[0]+=1
        elif name in jjj:
            ax.add_geometries(iter([x.geometry]),ccrs.PlateCarree(),
                      facecolor='r',
                      edgecolor=cl,linewidth=0.5)
            if k[1]==0:
                tmpl = mpatches.Rectangle((0, 0), 1, 1, facecolor='r',
                        label=cs[1])
                L.append(tmpl)
                k[1]+=1
        elif name in sdb:
            ax.add_geometries(iter([x.geometry]),ccrs.PlateCarree(),
                      facecolor='g',
                      edgecolor=cl,linewidth=0.5)
            if k[2]==0:
                tmpl = mpatches.Rectangle((0, 0), 1, 1, facecolor='g',
                        label=cs[2])
                L.append(tmpl)
                k[2]+=1
        elif name in csj:
            ax.add_geometries(iter([x.geometry]),ccrs.PlateCarree(),
                      facecolor='orange',
                      edgecolor=cl,linewidth=0.5)
            if k[3]==0:
                tmpl = mpatches.Rectangle((0, 0), 1, 1, facecolor='orange',
                        label=cs[3])
                L.append(tmpl)
                k[3]+=1
        elif name in zsj:
            ax.add_geometries(iter([x.geometry]),ccrs.PlateCarree(),
                      facecolor='yellow',
                      edgecolor=cl,linewidth=0.5)
            if k[4]==0:
                tmpl = mpatches.Rectangle((0, 0), 1, 1, facecolor='yellow',
                        label=cs[4])
                L.append(tmpl)
                k[4]+=1
        elif name in yma:
            ax.add_geometries(iter([x.geometry]),ccrs.PlateCarree(),
                      facecolor='pink',
                      edgecolor=cl,linewidth=0.5)
            if k[5]==0:
                tmpl = mpatches.Rectangle((0, 0), 1, 1, facecolor='pink',
                        label=cs[5])
                L.append(tmpl)
                k[5]+=1
        elif name in bbw:
            msk = [name.strip()==x.strip() for x in bbw]
            if np.sum(msk):
                ax.add_geometries(iter([x.geometry]),ccrs.PlateCarree(),
                                  facecolor='purple',
                                  edgecolor=cl,linewidth=0.5)
            if k[6]==0:
                tmpl = mpatches.Rectangle((0, 0), 1, 1, facecolor='purple',
                        label=cs[6])
                L.append(tmpl)
                k[6]+=1
    
    ax.set_xticks(np.arange(100,136,10), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(20,55,10), crs=ccrs.PlateCarree())
    lon_formatter = LongitudeFormatter(zero_direction_label=True)
    lat_formatter = LatitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)
    
    ax.set_extent([100,135,18,55],ccrs.PlateCarree())

    ax.tick_params(axis='both',labelfontfamily=fnamE)
    for ticks in ax.xaxis.get_major_ticks():
        ticks.label1.set_fontweight('bold')
    for ticks in ax.yaxis.get_major_ticks():
        ticks.label1.set_fontweight('bold')

    I = [1,2,6,0,4,5,3]
    L = np.array(L,dtype='object')
    ax.legend(handles=list(L[I]),prop={'family':fname,'size':8},
            loc='upper left',framealpha=1,edgecolor='k')
    ax.coastlines(resolution='50m')

    pos = ax._position
    dx = pos.x1-pos.x0
    dy = pos.y1-pos.y0
    cax = fig.add_axes([pos.x1-5*dx/12,pos.y0+dy/80,dx/3,dy/3],
            projection=ccrs.PlateCarree())
    cax.set_extent([105,125,2,28],ccrs.PlateCarree())
    cax.coastlines(resolution='10m')
    cax.add_geometries(shpsc.geometries(),ccrs.PlateCarree(),
                      facecolor='none',
                      edgecolor='k',linewidth=0.5)
    shpn = shpreader.Reader(r'F:\Linux\bourndarys_china\九段线.shp')
    cax.add_geometries(shpn.geometries(),ccrs.PlateCarree(),
                      facecolor='none',
                      edgecolor='r',linewidth=2)
    fig.savefig('csq.png',dpi=300,format='png',bbox_inches='tight')
    plt.show()




