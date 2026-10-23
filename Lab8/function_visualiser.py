import matplotlib.pyplot as plt


def plot_polynomial(a,b,c,xs):
    xplots=[]
    for x in xs:
        xplots.append(a*x**2 + b*x + c)

    plt.plot(xs,xplots)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'f(x) = {a}x^2 + {b}x + {c}')





if __name__ == "__main__":
    plot_polynomial(1, -5, 100, [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10])
    plt.show()  # ha gjerne plt.show() utenfor plot_polynomial