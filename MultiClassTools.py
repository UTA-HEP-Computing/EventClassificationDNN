import numpy as np
import h5py
from keras.utils import np_utils

def shuffle_in_unison_inplace(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def LoadData(Samples, FractionTest=.1, MaxEvents=-1, MinEvents=-1):
    FHandles={}
    Data={}
    ClassIndex={}
    ClassIndex0={}
    Instance={}

    # Get Data Out of every file
    index=0
    for S in Samples:
        if len(S)<3:
            S+=[0]

        if S[1] in Instance.keys():
            S[2]+=1
            Instance[S[1]]+=1
        else:
            Instance[S[1]]=0
            S[2]=0
            ClassIndex0[S[1]]=index
            index+=1

        SKey=S[1]+"_Inst"+str(S[2])

        f=h5py.File(S[0])
        Data[SKey]=f[S[1]]
        N=np.shape(Data[SKey])[0]

        print "Found",N," Events in",S,"."

        FHandles[SKey]=f

        ClassIndex[S[1]]=ClassIndex0[S[1]]

    print ClassIndex
    # MergeData and Create Labels

    First=True

    Train_X=None
    Train_Y=None

    Test_X=None
    Test_Y=None


    for SKey in Data:
        S=SKey.split("_Inst")[0]
        InstanceN=int(SKey.split("_Inst")[1])
        N=np.shape(Data[SKey])[0]
        N_Test=int(round(FractionTest*N))
        N_Train=N-N_Test

        if MaxEvents!=-1:
            if MaxEvents>N:
                print "Warning: Sample",S," has",N," events which is less that ",MaxEvents,"."
                print "Using ",N_Train,"Events for training."
                print "Using ",N_Test,"Events for training."
            else:
                N_Test=int(round(FractionTest*MaxEvents))
                N_Train=MaxEvents-N_Test

        if MinEvents!=-1:
            if N_Train<MinEvents:
                print "Warning: Sample",S," has",N_Train," training events which is less that ",MaxEvents,"."

        if not First:
            Train_X=np.concatenate((Train_X,Data[SKey][0:N_Train]))
            a=np.empty(N_Train); a.fill(ClassIndex[S])
            Train_Y=np.concatenate((Train_Y,a))

            Test_X=np.concatenate((Test_X,Data[SKey][-N_Test:]))
            a=np.empty(N_Test); a.fill(ClassIndex[S])
            Test_Y=np.concatenate((Test_Y,a))
        else:
            Train_X=Data[SKey][0:N_Train]
            a=np.empty(N_Train); a.fill(ClassIndex[S])
            Train_Y=a

            Test_X=Data[SKey][-N_Test:]
            a=np.empty(N_Test); a.fill(ClassIndex[S])
            Test_Y=a
            First=False        

        # Random Shuffle
     
    Train_X,Train_Y=shuffle_in_unison_inplace(Train_X,Train_Y)
    Test_X,Test_Y=shuffle_in_unison_inplace(Test_X,Test_Y)
        
    Train_Y= np_utils.to_categorical(Train_Y)
    Test_Y= np_utils.to_categorical(Test_Y)

    return (Train_X, Train_Y), (Test_X, Test_Y), ClassIndex



