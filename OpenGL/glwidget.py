from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt5.QtWidgets import QOpenGLWidget
from circuit import draw_circuit
#from scenario.scenario import

class GLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)


    def initializeGL(self):
        glClearColor(25/255, 25/255, 122/255, 1) # COR DO PLANO DE FUNDO  
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_NORMALIZE) # NORMALIZAÇÃO
        glEnable(GL_LIGHTING) # ATIVAÇÃO DA ILUMINAÇÃO

        '''
        ############# COMPONENTES DE FONTE DE LUZ #############
        '''

        '''
        # >>> FONTE DE LUZ DIRECIONAL - SOL
        '''
        # glEnable(GL_LIGHT0)
        # glLightfv(GL_LIGHT0, GL_AMBIENT, [0.9, 0.9, 0.9, 1.0])
        # glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.7, 0.7, 0.7, 1.0])
        # glLightfv(GL_LIGHT0, GL_SPECULAR, [1., 1., 1., 1.0])
        # glLightfv(GL_LIGHT0, GL_POSITION, [80, 120, 140, 1.0]) # POSIÇÃO ALEATÓRIA SETADA PARA O SOL
        # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [60, 0.03, 100]) # RAIO DE LUZ DIRECIONADO AO CENTRO DO CENÁRIO

        ''' 
        # >>> FONTE DE LUZ DIRECIONAL - LUA
        '''
        # glEnable(GL_LIGHT0)
        # glLightfv(GL_LIGHT0, GL_AMBIENT, [0.3, 0.3, 0.3, 1.0])
        # glLightfv(GL_LIGHT0, GL_DIFFUSE, [0., 0.1, 0.1, 1.0])
        # glLightfv(GL_LIGHT0, GL_SPECULAR, [0.1, 0.1, 0.1, 1.0])
        # glLightfv(GL_LIGHT0, GL_POSITION, [80, 120, 140, 1.0]) # POSIÇÃO ALEATÓRIA SETADA PARA O SOL
        # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [60, 0.03, 100]) # RAIO DE LUZ DIRECIONADO AO CENTRO DO CENÁRIO

        '''
        # >>> FONTE DE LUZ DIRECIONAL APAGADA
        '''
        # glEnable(GL_LIGHT0)
        # glLightfv(GL_LIGHT0, GL_AMBIENT, [0, 0, 0, 0])
        # glLightfv(GL_LIGHT0, GL_DIFFUSE, [0, 0, 0, 0])
        # glLightfv(GL_LIGHT0, GL_SPECULAR, [0, 0, 0, 0])
        # glLightfv(GL_LIGHT0, GL_POSITION, [80, 120, 140, 1.0])
        # glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [60, 0.03, 100]) # RAIO DE LUZ DIRECIONADO AO CENTRO DO CENÁRIO

        '''
        # >>> FONTE DE LUZ SPOT - NOITE(HELICOPTERO)
        '''
        # # ILUMINANDO A METADE SUPERIOR DO CENÁRIO
        glEnable(GL_LIGHT1)
        glLightfv(GL_LIGHT1, GL_AMBIENT, [0.7, 0.7, 0.7, 1.0])
        glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.7,0.7,0.7, 1.0])
        glLightfv(GL_LIGHT1, GL_SPECULAR, [0.7,0.7,0.7, 1.0])
        glLightfv(GL_LIGHT1, GL_POSITION, [82, 60, 50, 1]) # PONTO DA FONTE LUMINOSA
        glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [76.5, 0.03, 0]) # DIREÇÃO DO RAIO DE LUZ
        glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 90); # ANGULO DE ABERTURA DO RAIO DE LUZ

        # ILUMINANDO A METADE DIREITA/CENTRAL DO CENÁRIO
        glEnable(GL_LIGHT1)
        glLightfv(GL_LIGHT1, GL_AMBIENT, [0.7, 0.7, 0.7, 1.0])
        glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.7,0.7,0.7, 1.0])
        glLightfv(GL_LIGHT1, GL_SPECULAR, [0.7,0.7,0.7, 1.0])
        glLightfv(GL_LIGHT1, GL_POSITION, [82, 60, 50, 1]) # PONTO DA FONTE LUMINOSA
        glLightfv(GL_LIGHT1, GL_SPOT_DIRECTION, [43, 0.5, 155]) # DIREÇÃO DO RAIO DE LUZ
        glLightf(GL_LIGHT3, GL_SPOT_EXPONENT, 100)
        glLightf(GL_LIGHT1, GL_SPOT_CUTOFF, 60); # ANGULO DE ABERTURA DO RAIO DE LUZ


        '''
        # >>> FONTE DE LUZ PONTUAL - SIRENE DE ALARME
        '''
        
        # glEnable(GL_LIGHT2)
        # glLightfv(GL_LIGHT2, GL_AMBIENT, [0.35, 0, 0, 0.1])
        # glLightfv(GL_LIGHT2, GL_DIFFUSE, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT2, GL_SPECULAR, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT2, GL_POSITION, [40.7, 20, 74,1]) # PONTO DA FONTE LUMINOSA
        # glLightfv(GL_LIGHT2, GL_SPOT_DIRECTION, [60, 0.05, 74]) # [40,4,51]); #direcao da spotlight
        # glLightf(GL_LIGHT2, GL_SPOT_EXPONENT, 0); #concentracao da luz, maior abre mais
        # glLightf(GL_LIGHT2, GL_SPOT_CUTOFF, 30); # angulo de iluminaçao da spotlight
        # glEnable(GL_LIGHTING)

        # glEnable(GL_LIGHT3)
        # glLightfv(GL_LIGHT3, GL_AMBIENT, [0.35, 0, 0, 0.1])
        # glLightfv(GL_LIGHT3, GL_DIFFUSE, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT3, GL_SPECULAR, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT3, GL_POSITION, [40.7, 20, 74,1]) # PONTO DA FONTE LUMINOSA
        # glLightf(GL_LIGHT3, GL_SPOT_EXPONENT, 0); #concentracao da luz, maior abre mais
        # glLightf(GL_LIGHT3, GL_SPOT_CUTOFF, 30); # angulo de iluminaçao da spotlight
        # glEnable(GL_LIGHTING)

        # glEnable(GL_LIGHT4)
        # glLightfv(GL_LIGHT4, GL_AMBIENT, [0.35, 0, 0, 0.1])
        # glLightfv(GL_LIGHT4, GL_DIFFUSE, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT4, GL_SPECULAR, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT4, GL_POSITION, [40.7, 20, 74,1]) # PONTO DA FONTE LUMINOSA
        # glLightf(GL_LIGHT4, GL_SPOT_EXPONENT, 1); #concentracao da luz, maior abre mais
        # glLightf(GL_LIGHT4, GL_SPOT_CUTOFF, 15); # angulo de iluminaçao da spotlight
        # glEnable(GL_LIGHTING)

        # glEnable(GL_LIGHT5)
        # glLightfv(GL_LIGHT5, GL_AMBIENT, [0.35, 0, 0, 0.1])
        # glLightfv(GL_LIGHT5, GL_DIFFUSE, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT5, GL_SPECULAR, [0.35,0,0, 0.1])
        # glLightfv(GL_LIGHT5, GL_POSITION, [29.,4.3,75 ,1]) # PONTO DA FONTE LUMINOSA
        # glLightfv(GL_LIGHT5, GL_SPOT_DIRECTION, [43, 0.5, 155]) # DIREÇÃO DO RAIO DE LUZ
        # glLightf(GL_LIGHT5, GL_SPOT_CUTOFF, 15); # ANGULO DE ABERTURA DO RAIO DE LUZ
        # glEnable(GL_LIGHTING)
        

        '''
        # >>> FONTE DE LUZ SPOT - NOITE(FARÓIS) 
        '''
        # #Farol do Carro 02 - 
        # glEnable(GL_LIGHT6)
        # glLightfv(GL_LIGHT6, GL_AMBIENT, [0.1, 0.1, 0.1, 1.0])
        # glLightfv(GL_LIGHT6, GL_DIFFUSE, [1,1,1, 1.0])
        # glLightfv(GL_LIGHT6, GL_SPECULAR, [1,1,1, 1.0])
        # glLightfv(GL_LIGHT6, GL_POSITION, [40.,0.03,89 ,1]) # PONTO DA FONTE LUMINOSA
        # glLightfv(GL_LIGHT6, GL_SPOT_DIRECTION, [31, 0.03, 75]) # DIREÇÃO DO RAIO DE LUZ
        # glLightf(GL_LIGHT6, GL_SPOT_CUTOFF, 60); # ANGULO DE ABERTURA DO RAIO DE LUZ
        # glEnable(GL_LIGHTING)

        '''
        '''
         
        glLightModelfv(GL_LIGHT_MODEL_AMBIENT, [0.1, 0.1, 0.1])
        glEnable(GL_CULL_FACE) #Habilitado o Back Face Culling
        glFrontFace(GL_CCW)
        glShadeModel(GL_SMOOTH)

        '''
        ############# FIM DE FONTES DE LUZ #############
        '''

    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
             
        ''' ############## VISTAS [EYE POSITION, LOOK_AT POINT, VIEW_UP POINT] ############## '''

        '''
        # >>> VISTA DA ARQUIBANCADA
        '''

        # gluPerspective(100, (width/height), 5, 167)
        # gluLookAt(70,10,40, 70,1,80, 0,4,3)

        '''
        # >>> VISTA GERAL SUPERIOR (TERRENO COMPLETO)
        '''

        # glFrustum(-35, 50, -6, 8, 5, 60) #xmin, xmax,ymin,ymax,near,far
        # gluLookAt(37,37,50, 50,0,50, 0,1,0) # Vista de cima, posicionada acima da rua, pegando todo o perímetro da prisão
        
        '''
        # >>> VISTA DO FUNDO DO TERRENO
        '''
        # glFrustum(-35, 50, -6, 5, 5, 130) #ESQUERDA / DIREITA / BASE / ALTURA / NEAR / FAR
        # gluLookAt(117,20,80, 20,1,80, 0,1,0) # Vista do fundo, posicionada sobre à cerca, pegando 60% da prisão(árvore, arquibancada, campo e detentos)

        '''
        '''

        '''
        # >>> VISTA DA RUA (CANTEIRO INFERIOR)
        '''
        gluPerspective(125, (width/height), 2, 150)
        gluLookAt(11,4,30, 120,1,65, 0,1,0)

        '''
        # >>> VISTA DA ENTRADA DA PRISÃO (DENTRO DA PRISÃO)
        '''
        # gluPerspective(125, (width/height), 1, 80)
        # gluLookAt(35,3,150, 120,1,150, 0,1,0)

        '''
        # >>> VISTA PARALELA À ARQUIBANCADA
        '''
        # gluPerspective(100, (width/height), 5, 167)
        # gluLookAt(90,10,145, 60,1,80, 0,1,0)

        '''
        ############# FIM DAS VISTAS #############
        '''
        
        ## Projeção Ortogonal
        #glOrtho(-15, 15, -2, 15, 5, 80)


    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()

        draw_circuit()

        
  
       