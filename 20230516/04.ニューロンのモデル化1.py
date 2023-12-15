def f_04_ニューロンのモデル化():
    # P24 ニューラルネットワーク（2層）の出力値の計算
    def f(w1, x1, w2, x2, b):
        return w1 * x1 + w2 * x2 + b

    x1, x2 = 0.8, 0.4
    b1, b2 = 0.0, 0.0
    w11, w21 = 0.6, 0.2
    w12, w22 = 0.4, 0.7
    a1 = f(w1=w11, w2=w21, x1=x1, x2=x2, b=b1)
    a2 = f(w1=w12, w2=w22, x1=x1, x2=x2, b=b2)
    print("# No.1 ###############################")
    print("a1=", a1)
    print("a2=", a2)
    ####################################################################################
    # P26 ニューラルネットワーク（3層）の出力値の計算
    w_list = [
        [0.2, 0.5],
        [0.3, 0.4],
        [0.7, 0.8]
    ]
    x_list = [0.8,
              0.4]
    b_list = [0.2,
              0.5,
              0.4]
    #! C:\400_Python\myenv\Scripts\python.exe
    
    import numpy as np
    w = np.array(w_list)
    x = np.array(x_list)
    b = np.array(b_list)
    a = np.dot(w, x) + b
    aa = w @ x + b # np.dot(w, x) + b　と同じ

    print("# No.2 ###############################")
    print("type(w)=", type(w))
    print("w.shape=", w.shape)
    print("w=", w)
    print("----------------------")
    print("type(x)=", type(x))
    print("x.shape=", x.shape)
    print("x=", x)
    print("----------------------")
    print("type(b)=", type(b))
    print("b.shape=", b.shape)
    print("b=", b)
    print("----------------------")
    print("type(a)=", type(a))
    print("a.shape=", a.shape)
    print("a=", a)
    print("----------------------")
    print("type(aa)=", type(aa))
    print("aa.shape=", aa.shape)
    print("aa=", a)
    print("----------------------")
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))
    print("sigmoid(a)=", sigmoid(a))


if __name__ == "__main__":
    f_04_ニューロンのモデル化()
