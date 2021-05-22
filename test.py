import scipy.io as scio
matpath = './md_test_v2.mat'
data = scio.loadmat(matpath)

print(data)