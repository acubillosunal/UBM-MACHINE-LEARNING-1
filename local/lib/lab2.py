"""
Este archivo es generado automaticamente.
###### NO MODIFICAR #########
# cualquier alteración del archivo
# puede generar una mala calficacion o configuracion
# que puede repercutir negativamente en la 
# calificacion del laboratorio!!!!!
"""
from local.lib.imports import *
from scipy.stats import mode
from sklearn.model_selection import train_test_split, StratifiedKFold, KFold
from numpy import random
from sklearn.preprocessing import StandardScaler
from scipy.spatial.distance import euclidean
from scipy.spatial.distance import cdist

@unknow_error
def test_muestras_por_clases(func):
    ones = func( np.ones(10))
    five = func( np.array([10,20,30,40,50]))

    tests = {'recuerda retornar un diccionario': isinstance(ones, dict) and isinstance(five, dict),
             'el numero de clases es equivalente a los valores unicos en Y': len(ones) == 1 and len(five) == 5,
             'recuerda que las claves deben ser las etiquetas': list(ones.keys()) == [1] and list(five.keys()) == [10,20,30,40,50]
             }
    test_res = ut.test_conditions_and_methods(tests)
    return (test_res)

@unknow_error
def test_KNN_Clasificacion(func):
   
    xtrains = np.array([[0,1], [1,1], [-1,1], [-1,0], [-0.9,0.15]])
    ytrains =  np.array([0,0,1,1,1])
    xtests = np.array([[0.01,0.9], [0.9,0.9], [-0.99,0.99], [-0.8,-0.1]])

    ytests_should2 = np.array([0., 0., 1., 1.])
    ytests_should3 = np.array([0., 0., 1., 1.])
    ytests_should5 = np.array([1., 1., 1., 1.])
    dists =  np.array([[0.10049876, 0.99503769, 1.01493842, 1.35281189, 1.17923704],
                      [0.90553851, 0.14142136, 1.90262976, 2.1023796 , 1.95      ],
                      [0.9900505 , 1.99002513, 0.01414214, 0.9900505 , 0.84480767],
                      [1.36014705, 2.10950231, 1.11803399, 0.2236068 , 0.26925824]])
    
    lr1, dr1 =  func(np.random.rand(10,2),  np.random.choice(2,10), np.random.rand(3,2), 5)
    lr2, dr2 =  func(np.random.rand(10,2),  np.random.choice(2,10), np.random.rand(3,2), 5)
    r2 =  func(xtrains, ytrains, xtests, 2)
    r3 =  func(xtrains, ytrains, xtests, 3)
    r5 =  func(xtrains, ytrains, xtests, 5)
    t2 =  ut.are_np_equal(r2[1], dists) and ut.are_np_equal(r2[0], ytests_should2) 
    t3 =  ut.are_np_equal(r3[1], dists) and ut.are_np_equal(r3[0], ytests_should3) 
    t5 =  ut.are_np_equal(r5[1], dists) and ut.are_np_equal(r5[0], ytests_should5)
    tr1 = ut.are_np_equal(dr1, dr2, True) and (dr1.shape == (3,10))
    #
    tests = {'test 1 fallo': t2,
             'test 2 fallo': t3,
             'test 3 fallo': t5,
             'test 4 fallo': tr1,
             
             }
    test_res = ut.test_conditions_and_methods(tests)

    return (test_res)

@unknow_error
def test_train_test_split_fix(func):
    x1,x2,y1,y2 = func(np.random.rand(10,2),np.random.choice(2,10))
    x11,x21,y11,y21 = func(np.random.rand(50,3),np.random.choice(2,50))

    tests = {'test 1 fallo': x1.shape == (7,2) and x2.shape == (3,2) and y1.shape[0] == 7 and y2.shape[0] == 3,
             'test 2 fallo': x11.shape == (35,3) and x21.shape == (15,3) and y11.shape[0] == 35 and y21.shape[0] == 15 
            }
    return (ut.test_conditions_and_methods(tests))

@unknow_error
def test_exp(func):
    xx = np.array([[0,1], [1,1], [-1,1], [-1,0], [-0.9,0.15], [0.01,0.9], [0.9,0.9], [-0.99,0.99], [-0.8,-0.1]])
    yy =  np.array([0,0,1,1,1, 1,1,1,1])
    ks = [1,2,3,4]  
    res = ut.test_experimento_oneset(func,  shape_val=(len(ks), 2), 
                                    col_error = ['error de prueba'],
                                    col_val=['k-vecinos', 'error de prueba'],
                                    X = xx, Y=yy,
                                    ks = ks)
    code_to_look = ['KNN_Clasificacion', "ErrorClas"]
    res2 = ut.check_code(code_to_look, func, "recuerda usar las funciones anteriores!")
    return (res and res2)

@unknow_error
def test_parzenClass(func):
   
    xtrains = np.array([[0.1,0.1], [0.2,0.19], [0.75,0.85],  [1,1], [0.1,0.8], [0.9,0.15]])
    ytrains =  np.array([0,0,2,2,1,1])
    xtests = np.array([[0.25,0.35], [0.9,0.9], [0.1,0.9]])

    ytests_should1 = np.array([0., 2., 1.])
    ytests_should2 = np.array([0., 2., 0.])
    fdp1 =  np.array([[9.99949903e-01,5.00969531e-05, 5.34883453e-11],
                     [3.95876950e-22, 9.44208061e-13, 1.00000000e+00],
                     [1.13346559e-11, 9.99999999e-01, 9.73620033e-10]])
    
    fdp2 = np.array([[0.38722464, 0.33598465, 0.27679071],
                    [0.24737782, 0.3218237,  0.43079848],
                    [0.3321231,  0.34179345, 0.32608345]])

    fdp3 = np.array([[0.33387398, 0.33339494, 0.33273108],
                    [0.3324197,  0.33330303, 0.33427727],
                    [0.33337427, 0.33332707, 0.33329866]])
    clf = func(0.1).fit(xtrains, ytrains)
    l1,f1 =  clf.predict(xtests)
    clf = func(1).fit(xtrains, ytrains)
    l2,f2 =  clf.predict(xtests)
    clf = func(10).fit(xtrains, ytrains)
    l3,f3 =  clf.predict(xtests)

    t1 =  ut.are_np_equal(l1, ytests_should1) and ut.are_np_equal(f1, fdp1)
    t2 =  ut.are_np_equal(l2, ytests_should1) and ut.are_np_equal(f2, fdp2)
    t3 =  ut.are_np_equal(l3, ytests_should2) and ut.are_np_equal(f3, fdp3)

    tests = {'test 1 fallo': t2,
             'test 2 fallo': t3,
             'test 3 fallo': t3,
              
             }
    test_res = ut.test_conditions_and_methods(tests)

    return (test_res)

@unknow_error
def test_parzen_exp(func):
    xx = np.array([[0,1], [1,1], [-1,1], [-1,0], [-0.9,0.15], [0.01,0.9], [0.9,0.9], [-0.99,0.99], [-0.8,-0.1]])
    yy =  np.array([0,0,0,0,1, 1,1,1,1])
    hs = [0.1,1,5]    
    res = ut.test_experimento_oneset(func,  shape_val=(len(hs), 3), 
                                    col_error = ['error de prueba(media)', 'error de prueba(desviación estandar)'],
                                    col_val=['ancho de ventana', 'error de prueba(media)', 'error de prueba(desviación estandar)'],
                                    X = xx, Y=yy,
                                    hs = hs)
    code_to_look = ['parzenClass', "ErrorClas"]
    res2 = ut.check_code(code_to_look, func, "recuerda usar las funciones anteriores!")
    return (res and res2)


def part_1 ():
#cargamos la bd iris desde el dataset de sklearn
    from sklearn.datasets import load_digits
    digits = load_digits()
    x, y = digits.data, digits.target
    GRADER = Grader("lab2_part1")
    GRADER.add_test("ejercicio1.1", Tester(test_muestras_por_clases))
    GRADER.add_test("ejercicio1.2", Tester(test_parzenClass))
    #GRADER.add_test("ejercicio3", Tester(test_train_test_split_fix)),
    #GRADER.add_test("ejercicio4", Tester(test_exp))
    #GRADER.add_test("ejercicio5", Tester(test_parzenClass))
    #GRADER.add_test("ejercicio6", Tester(test_parzen_exp))
    return(GRADER, x,y)

@unknow_error
def test_plot_hist_and_get_freq_int(func):
    from sklearn.datasets import load_boston
    _, yy = load_boston(return_X_y=True)
    inf,sup, freq, f = func(yy[0:50])
    hist_t = len(f.axes[0].patches) == 10
    inf2,sup2, freq2, _ = func(np.ones(10))
    tests = {'test 1 fallo': (inf,sup, freq) == (12.7, 15.05, 11.0),
            'recueda usar la funcion de matplotlib y dejar la cuarta expresion en el return': hist_t,
            'test 3 fallo': (inf2,sup2, freq2,) == (1.0, 1.1, 10.0)
            }
    return (ut.test_conditions_and_methods(tests))

@unknow_error
def test_KNN_regresion(func):
    xtrains = np.array([[0,1], [1,1], [-1,1], [-1,0], [-0.9,0.15]])
    ytrains =  np.array([0.1,0.25,0.9,0.85,0.5])
    xtests = np.array([[0.01,0.9], [0.9,0.9], [-0.99,0.99], [-0.8,-0.1]])

    ytests_should1 = np.array([0.175, 0.175, 0.7  , 0.675])
    ytests_should2 = np.array([0.52, 0.52, 0.52, 0.52])
    dists =  np.array([[0.10049876, 0.99503769, 1.01493842, 1.35281189, 1.17923704],
                        [0.90553851, 0.14142136, 1.90262976, 2.1023796 , 1.95      ],
                        [0.9900505 , 1.99002513, 0.01414214, 0.9900505 , 0.84480767],
                        [1.36014705, 2.10950231, 1.11803399, 0.2236068 , 0.26925824]])
    
    lr1, dr1 =  func(np.ones((10,2)), np.random.choice(1,10), np.random.choice(1,6).reshape((3,2)), 2)
    r1 =  func(xtrains, ytrains, xtests, 2)
    r2 =  func(xtrains, ytrains, xtests, 5)
    t1 =  ut.are_np_equal(r1[1], dists) and ut.are_np_equal(r1[0], ytests_should1) 
    t2 =  ut.are_np_equal(r2[1], dists) and ut.are_np_equal(r2[0], ytests_should2) 
    tr1 = np.sum(dr1) != np.sum(r1[1]) and (dr1.shape == (3,10))
    #
    tests = {'test 1 fallo': t1,
             'test 2 fallo': t2,
             'test 3 fallo': tr1 }

    return ( ut.test_conditions_and_methods(tests))


@unknow_error
def test_knn_reg_exp(func):
    xx = np.array([[0,1], [1,1], [-1,1], [-1,0], [-0.9,0.15], [0.01,0.9], [0.9,0.9], [-0.99,0.99], [-0.8,-0.1]])
    yy =  np.array([0.1,0.2,0.5,0.3,0.7, 0.65,0.9,0.9,0.9])
    ks = [2,3,5]    
    res = ut.test_experimento_oneset(func,  shape_val=(len(ks), 3), 
                                    col_error = ['error de prueba(media)', 'error de prueba(desviación estandar)'],
                                    col_val=['k-vecinos', 'error de prueba(media)', 'error de prueba(desviación estandar)'],
                                    X = xx, Y=yy,
                                    ks = ks)
    code_to_look = ['KNN_regresion', "MAPE"]
    res2 = ut.check_code(code_to_look, func, "recuerda usar las funciones anteriores!")
    return (res and res2)

@unknow_error
def test_KNN_regresion_parzen(func):
    xtrains = np.array([[0,1], [1,1], [-1,1], [-1,0], [-0.9,0.15]])
    ytrains =  np.array([0.1,0.25,0.9,0.85,0.5])
    xtests = np.array([[0.01,0.9], [0.9,0.9], [-0.99,0.99], [-0.8,-0.1]])

    ytests_should2 = np.array([0.10638661, 0.24730208, 0.88310823, 0.68507659])
    ytests_should1 = np.array([0.50582812,0.47094519,0.54219998,0.54804124]) 
    #rr1 =  func(np.ones((10,2)), np.random.choice(1,10), np.random.choice(1,6).reshape((3,2)), 2)
    #r1 =  func(xtrains, ytrains, xtests, 0.1)
    #r2 =  func(xtrains, ytrains, xtests, 5)

    clf = func(2).fit(np.ones((10,2)), np.random.choice(1,10))
    rr1 =  clf.predict(np.random.choice(1,6).reshape((3,2)))
   
    clf = func(0.1).fit(xtrains, ytrains)
    r1 =  clf.predict(xtests)

    clf = func(5).fit(xtrains, ytrains)
    r2 =  clf.predict(xtests)

    t1 = ut.are_np_equal(r1, ytests_should1) 
    t2 = ut.are_np_equal(r2, ytests_should2) 
    tr1 = np.sum(rr1) != np.sum(r1)

    tests = {'test 1 fallo': t1,
             'test 2 fallo': t2,
             'test 3 fallo': tr1 }

    return ( ut.test_conditions_and_methods(tests))


@unknow_error
def test_knn_reg_exp_parzen(func):
    xx = np.array([[0,1], [1,1], [-1,1], [-1,0], [-0.9,0.15], [0.01,0.9], [0.9,0.9], [-0.99,0.99], [-0.8,-0.1]])
    yy =  np.array([0.1,0.2,0.5,0.3,0.7, 0.65,0.9,0.9,0.9])
    hs = [1,2,3,5]    
    res = ut.test_experimento_oneset(func,  shape_val=(len(hs), 4), 
                                    col_error = ['error de prueba(media)', 'error de prueba(desviación estandar)'],
                                    col_val=['ancho de ventana', 'error de prueba(media)', 'error de prueba(desviación estandar)',
                                             'muestras en conjunto de pruebas (media)'],
                                    X = xx, Y=yy,
                                    hs = hs)
    t2 = func(xx, yy, [1, 2])['muestras en conjunto de pruebas (media)'].mean() != 2.25
    if t2:
        print("revisa tu, implementación, recuerda que debes usar la función para validación")

    code_to_look = ['Nadaraya_Watson', "MAPE", "[train", "[test"]
    res2 = ut.check_code(code_to_look, func, "recuerda usar las funciones anteriores y las sugeridas!")
    return (res and not(t2) and res2)



def part_2 ():
#cargamos la bd iris desde el dataset de sklearn
    from sklearn.datasets import load_boston
    x, y = load_boston(return_X_y=True)
    GRADER = Grader("lab2_part2")
    GRADER.add_test("ejercicio2.1", Tester(test_plot_hist_and_get_freq_int))
    #GRADER.add_test("ejercicio2", Tester(test_KNN_regresion))
    #GRADER.add_test("ejercicio3", Tester(test_knn_reg_exp))
    GRADER.add_test("ejercicio2.2", Tester(test_KNN_regresion_parzen))
    #GRADER.add_test("ejercicio5", Tester(test_knn_reg_exp_parzen))
    return(GRADER, x,y)
