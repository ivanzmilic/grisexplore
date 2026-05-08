# Code recieved by J.C. Trelles on 16/07/2025


def readmaps(file_path):

# Read GRIS maps and separate them into stokes profiles
# input--> file_path: path of the file to be read
# output --> stokes_I ,stokes_Q, stokes_U, stokes_V
# stokes_I, stokes_Q, stokes_U, stokes_V = readmaps('file_path')

    import numpy as np
    from astropy.io import fits
    import glob
    name=file_path
    files=sorted(glob.glob(name))
    n=0
    for i in range(len(glob.glob(name))):
        data=fits.getdata(files[i])
        n=n+np.shape(data)[0]/4.
    stokes_I=np.zeros((int(n), np.shape(data)[1],np.shape(data)[2]))
    stokes_Q=np.zeros((int(n), np.shape(data)[1],np.shape(data)[2]))
    stokes_U=np.zeros((int(n), np.shape(data)[1],np.shape(data)[2]))
    stokes_V=np.zeros((int(n), np.shape(data)[1],np.shape(data)[2]))
    if len(np.shape(data)) == 3:
        n=0
        for i in range(len(glob.glob(name))):
            data=fits.getdata(files[i][:])
            print(i)
            for j in range(int(np.shape(data)[0]/4.)):
                stokes_I[j+n,:,:]=data[j*4,:,:]
                stokes_Q[j+n,:,:]=data[j*4+1,:,:]
                stokes_U[j+n,:,:]=data[j*4+2,:,:]
                stokes_V[j+n,:,:]=data[j*4+3,:,:]
            n=int(np.shape(data)[0]/4.)+n
    elif len(np.shape(data)) == 4:
        stokes_I=data[0,:,:,:]
        stokes_Q=data[1,:,:,:]
        stokes_U=data[2,:,:,:]
        stokes_V=data[3,:,:,:]

    return stokes_I, stokes_Q, stokes_U, stokes_V 