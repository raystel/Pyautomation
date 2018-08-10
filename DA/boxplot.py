import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

# 正常显示中文
plt.rcParams['font.sans-serif'] = ['Simhei']

# 颜色配置
COLOR_1 = 'blue'
COLOR_2 = 'red'
# 图像配置
fig = plt.figure(figsize=(60, 60), dpi=200)
rcParams["pdf.fonttype"] = 42
# 字体配置
rcParams.update({'font.size': 20, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})

# 坐标配置
plt.ylabel('gene')
plt.title('GENE DATA')
# 读取文件
data_path = r'C:\Users\wisdom\PycharmProjects\htf_files_info\prepare_for_boxplot.txt'
df = pd.read_csv(data_path, index_col='gene', sep='\t')
# 基因分组列选取
red_box = df[
    ['BIBR1', 'BIBR2', 'BIBR3', 'BIBR4', 'BIBR5', 'BIBR6', 'BIBR7', 'BIGI1', 'BIGI2', 'BIGI3', 'BIGI3', 'BIGI4',
     'BIGI5', 'BIGI6', 'BINE1', 'BINE2', 'BINE3', 'BINE4', 'BINE5', 'BINE6', 'BINE7', 'BINE8', 'BTAN1', 'BTAN10',
     'BTAN11', 'BTAN12', 'BTAN13', 'BTAN14', 'BTAN15', 'BTAN16', 'BTAN2', 'BTAN3', 'BTAN4', 'BTAN5', 'BTAN6', 'BTAN7',
     'BTAN8', 'BTAN9', 'BTHO1', 'BTHO10', 'BTHO11', 'BTHO12', 'BTHO13', 'BTHO14', 'BTHO15', 'BTHO16', 'BTHO17',
     'BTHO18', 'BTHO19', 'BTHO2', 'BTHO20', 'BTHO21', 'BTHO22', 'BTHO3', 'BTHO4', 'BTHO5', 'BTHO6', 'BTHO7', 'BTHO8',
     'BTHO9', 'BTJE1', 'BTJE2', 'BTJE3', 'BTJE4', 'BTJE5', 'BTJE6', 'BTLM1', 'BTLM2', 'BTLM3', 'BTLM4', 'BTLM5',
     'BTLM6', 'BTRO1', 'BTRO2', 'BTRO3', 'BTRO4']]
blue_box = df[
    ['PC1', 'ITWB1', 'ITWB2', 'ITWB3', 'ITWB4', 'ITWB5', 'ITWB6', 'ITWB7', 'ITWB8', 'ITWB10', 'ITWB11', 'ITWB12',
     'ITWB13', 'ITWB14', 'ITWB15']]
# 将数据导入箱图
b = plt.boxplot(blue_box, labels=blue_box.index, patch_artist=True, vert=False, showcaps=True,
                # 异常值设置
                flierprops={'marker': '.', 'markerfacecolor': COLOR_1, 'color': COLOR_1, 'markeredgecolor': COLOR_1,'linewidth':0.5},
                # 箱体设置
                boxprops={'color': COLOR_1, 'facecolor': COLOR_1, 'linestyle': '--', 'alpha': 0.5},
                # 中间轴线设置
                capprops={'color': COLOR_1, 'linewidth': '1.0', 'linestyle': '-'},
                # 尾端须线设置
                whiskerprops={'color': COLOR_1, 'linestyle': '--', 'linewidth': 1.0})
# 箱体颜色线条设置
for patch in b['boxes']:
    patch.set(color=COLOR_1, linewidth=0.5)
for median in b['medians']:
    median.set(color=COLOR_1, linewidth=1.5)

r = plt.boxplot(red_box, labels=red_box.index, patch_artist=True, vert=False, showcaps=True,
                flierprops={'marker': '.', 'markerfacecolor': COLOR_2, 'color': COLOR_2, 'markeredgecolor': COLOR_2},
                boxprops={'color': COLOR_2, 'facecolor': COLOR_2, 'linestyle': '--', 'alpha': 0.5},
                capprops={'color': COLOR_2, 'linewidth': '1.0', 'linestyle': '-'},
                whiskerprops={'color': COLOR_2, 'linestyle': '--', 'linewidth': 1.0})
for patch in r['boxes']:
    patch.set(color=COLOR_2, linewidth=0.5)
for median in r['medians']:
    median.set(color=COLOR_2, linewidth=1.5)
# 保存PDF
plt.savefig('gene.pdf', format='pdf')
# 显示图形
plt.show()
