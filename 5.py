import numpy as np
def createMatrix(m):
    # Membuat matrix ordo mxm
    mtrx = np.random.randint(1,99,size=(m,m))
    
    # Mengubah arah diagonal matrix yang semula berawal dari kanan atas menjadi berawal dari kiri atas
    mtrx2 = np.fliplr(mtrx)
    
    # Jumlah diagonal matrix yang mulai dari kiri atas (diagonal 1)
    jmlhDMtrx = np. trace(mtrx)
    # Jumlah diagonal matrix yang mulai dari kanan atas (diagonal 2)
    jmlhDMtrx2 = np.trace(mtrx2)
    #jumlah kedua diagonal (diagonal 1 + diagonal 2)
    jmlhD = jmlhDMtrx + jmlhDMtrx2
    print(mtrx)
    print("Total:",jmlhD)

createMatrix(3)