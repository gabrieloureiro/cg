from OpenGL.GL import *
from objetos import obj
def draw_circuit():
    rgb_wall_material = [44/255, 137/255, 142/255]
    rgb_vermelho = [1,0,0]
    rgb_azul = [0,0,1]
    gramado = [50/255, 205/255, 50/255]
    folhas = [50/255, 140/255, 50/255]
    solo = [151/255,105/255,79/255]
    arvore = [92/255, 51/255, 23/255]
    aço = [168/255, 168/255, 168/255]
    cal = [1,1,1]
    asfalto = [76/255,76/255,76/255]
    listra = [217/255, 217/255, 25/255]
    detento = [217/255, 135/255, 25/255]
    lixeira = [35/255, 107/255, 142/255]
    latao = [33/255, 94/255, 33/255]
    azul = obj.Material(rgb_azul, rgb_azul, [0.3,0.3,0.3], 10)
    vermelho = obj.Material(rgb_vermelho, rgb_vermelho, [0.3,0.3,0.3], 10)
    grama = obj.Material(gramado, gramado, [0.3,0.3,0.3], 10)
    madeira = obj.Material(arvore,arvore, [0.3,0.3,0.3],10)
    cal = obj.Material(cal,cal, [0.3,0.3,0.3],10)
    terra = obj.Material(solo, solo, [0.1,0.1,0.1], 10)
    ferro = obj.Material(aço, aço, [0.3,0.3,0.3], 10)
    espelho = obj.Material([0.8,0.8,0.8], [0,0,0], [0.8,0.8,0.8], 20)
    

    # OBJETOS QUE COMPÕEM O CENÁRIO

    # Chão
    glPushMatrix()
    glScalef(150.,0.01, 200.)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', terra)
    draw_polygon(cube)
    glPopMatrix()

    # Campo
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', grama)
    glTranslatef(65 ,0., 52)
    glScalef(40, 0.02, 78)
    draw_polygon(cube)
    glPopMatrix()

     # Reta Esquerda
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal)
    glTranslatef(65 ,0., 51)
    glScalef(40, 0.1, 1)
    draw_polygon(cube)
    glPopMatrix()
    
    # Reta Direita
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal)
    glTranslatef(65 ,0., 130)
    glScalef(40, 0.1, 1)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Inferior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal)
    glTranslatef(65 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Central
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal)
    glTranslatef(86 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Reta Superior
    glPushMatrix()
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', cal)
    glTranslatef(105 ,0., 51)
    glScalef(0.5, 0.1, 79)
    draw_polygon(cube)
    glPopMatrix()

    # Carro 01 - Dentro do Terreno
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(58.,4.3,175.)
    glScalef(1,1.8,2)
    glRotatef(90,0,1,0)
    objeto('objetos/camaro.obj')
    glPopMatrix()

    # Carro 02 - Entrando no terreno
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(29.,4.3,75.)
    glScalef(1,1.8,2)
    glRotatef(193,0,1,0)
    objeto('objetos/camaro.obj')
    glPopMatrix()

    # Sirene 01
    glPushMatrix()
    glTranslatef(55.5, 6, 172)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', vermelho)
    draw_polygon(cube)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(55.5, 6, 175)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', azul)
    draw_polygon(cube)
    glPopMatrix()

    # Sirene 02
    glPushMatrix()
    glTranslatef(26.7, 6, 72)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', vermelho)
    draw_polygon(cube)
    glPopMatrix()

    glPushMatrix()
    glTranslatef(26.7, 6, 75)
    glScalef(3, 1, 3)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', azul)
    draw_polygon(cube)
    glPopMatrix()

    # Arquibancada:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, arvore)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, arvore)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, arvore)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(71, 0.05, 25)
    glScalef(2.108,1,1.8)
    objeto('objetos/grandstand.obj')
    glPopMatrix()

    #Asfalto
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, asfalto)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, asfalto)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(22, 0.01, 99)
    glScalef(2.7,0.02,23)
    objeto('objetos/road.obj')
    glPopMatrix()

    #Linha do asfalto
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, listra)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, listra)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, listra)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(22, 0.01, 99)
    glScalef(0.2,0.05,23)
    objeto('objetos/road.obj')
    glPopMatrix()

    #Canteiro inferior
    glPushMatrix()
    glTranslatef(15, 0.01, 1)
    glScalef(1, 1, 192)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()

    #Canteiro superior
    glPushMatrix()
    glTranslatef(28, 0.06, 116)
    glScalef(1, 1, 80)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()

    #Folhas Arvore:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, folhas)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, folhas)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 20)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeLeaves.obj')
    glPopMatrix()

    # Caule Arvore:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, arvore)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, arvore)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, arvore)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 20)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeStem.obj')
    glPopMatrix()

    # Caule Arvore2:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, arvore)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, arvore)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, arvore)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(106, 0.1, 173)
    glScalef(1,0.5,1.5)
    objeto('objetos/MapleTreeStem.obj')
    glPopMatrix()

    # Cerca direita
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, aço)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(75.7, 0.01, 199)
    glScalef(5,0.7,10)
    #glRotatef(90,0,1,0)
    objeto('objetos/fance.obj')
    glPopMatrix()

    # Portão
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, aço)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(28.8, 0.01, 75)
    glScalef(1.7,0.7,6.8)
    glRotatef(90,0,1,0)
    objeto('objetos/military_fence_gate.obj')
    glPopMatrix()

    # Cerca Fundo
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, aço)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(112, 0.01, 98.2)
    glScalef(4,0.7,12.5)
    glRotatef(90,0,1,0)
    objeto('objetos/fance.obj')
    glPopMatrix()

    # Cerca Esquerda
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, aço)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(75.7, 0.01, 0)
    glScalef(5,0.7,10)
    #glRotatef(90,0,1,0)
    objeto('objetos/fance.obj')
    glPopMatrix()

    #Torre do vigia
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, aço)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, aço)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(40.7, 0.01, 74)
    glScalef(2,2.6,3)
    glRotatef(180,0,1,0)
    objeto('objetos/wooden_watch_tower2.obj')
    glPopMatrix()

    # Alarme
    glPushMatrix()
    glTranslatef(40.7, 20, 74)
    glScalef(0.5, 2.2, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', vermelho)
    draw_polygon(cube)
    glPopMatrix()

    # Detento 1
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, detento)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(90, 0.1, 120)
    glScalef(1.5,1,2.7)
    glRotatef(270,0,1,0)
    objeto('objetos/male.obj')
    glPopMatrix()

    # Detento 2
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, detento)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, detento)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(75, 0.1, 75)
    glScalef(1.5,1,2.7)
    glRotatef(90,0,1,0)
    objeto('objetos/male.obj')
    glPopMatrix()

    #Policial 1
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(58, 0.1, 85)
    glScalef(1.5,1,2.7)
    glRotatef(270,0,1,0)
    objeto('objetos/male.obj')
    glPopMatrix()

    # Bola
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(90, 2, 80)
    glScalef(1.3,0.5,3.05)
    #glRotatef(90,0,1,0)
    objeto('objetos/Ball.obj')
    glPopMatrix()

    # Lixeira Azul
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, lixeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, lixeira)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, lixeira)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(40, 0.05, 50)
    glScalef(0.03,0.03,0.1)
    glRotatef(90,0,1,0)
    objeto('objetos/trash.obj')
    glPopMatrix()

    # Lixeira Verde
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, latao)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, latao)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, latao)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(40, 0.05, 20)
    glScalef(0.03,0.03,0.1)
    glRotatef(90,0,1,0)
    objeto('objetos/trash.obj')
    glPopMatrix()

    #Banco Up Left:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, latao)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, latao)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, latao)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(108.5, 0.1, 75)
    glScalef(0.08,0.04,0.12)
    glRotatef(270,0,1,0)
    objeto('objetos/Bench_HighRes.obj')
    glPopMatrix()

    #Banco Up Right:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, rgb_vermelho)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, rgb_vermelho)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, rgb_vermelho)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(108.5, 0.1, 118)
    glScalef(0.08,0.04,0.12)
    glRotatef(270,0,1,0)
    objeto('objetos/Bench_HighRes.obj')
    glPopMatrix()
    
    #Hidrante:
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0.3,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0.3,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0.3,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 1)
    glPushMatrix()
    glTranslatef(30, 0.03, 13)
    glScalef(0.07,0.07,0.07)
    glRotatef(270,1,0,0)
    objeto('objetos/hidra.obj')
    glPopMatrix()

    ##TRAVE INFERIOR - VERTICAL ESQUERDA
    glPushMatrix()
    glTranslatef(67, 0, 75)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE INFERIOR - VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(67, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE INFERIOR - HORIZONTAL
    glPushMatrix()
    glTranslatef(67, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()


    ##TRAVE SUPERIOR - VERTICAL ESQUERDA
    glPushMatrix()
    glTranslatef(100, 0, 75)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE SUPERIOR - VERTICAL DIREITA
    glPushMatrix()
    glTranslatef(100, 0, 105)
    glScalef(1, 5, 1)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()

    ##TRAVE SUPERIOR - HORIZONTAL
    glPushMatrix()
    glTranslatef(100, 5, 75)
    glScalef(1, 1, 31)
    cube = obj.Obj().import_obj('../objects/cube_vn.obj', ferro)
    draw_polygon(cube)
    glPopMatrix()

    # SOL
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, listra)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, listra)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, listra)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(80, 120, 140)
    glScalef(2,2,3)
    #glRotatef(90,0,1,0)
    objeto('objetos/Ball.obj')
    glPopMatrix()

    # LUA
    # glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, aço)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, aço)
    # glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, aço)
    # glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    # glPushMatrix()
    # glTranslatef(80, 120, 140)
    # glScalef(2,2,3)
    # #glRotatef(90,0,1,0)
    # objeto('objetos/Ball.obj')
    # glPopMatrix()

    # HELICOPTERO
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, [0,0,0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, [0,0,0])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, 3)
    glPushMatrix()
    glTranslatef(76.5, 80, 55)
    glScalef(5,2.5,4)
    glRotatef(210,1,1,0)
    glRotatef(37,1,0,0)
    objeto('objetos/uh60.obj')
    glPopMatrix()



# Função polígonos 
def draw_polygon(obj):
    for face in obj.faces:
        glMaterialfv(GL_FRONT, GL_AMBIENT, face.material.k_a_rgb)
        glMaterialfv(GL_FRONT, GL_DIFFUSE, face.material.k_d_rgb)
        glMaterialfv(GL_FRONT, GL_SPECULAR, face.material.k_e_rgb)
        glMaterialf(GL_FRONT, GL_SHININESS, face.material.attenuation)

        glBegin(GL_POLYGON)
        for vertex in face.vertices:
            glNormal3fv(vertex.normal)
            glVertex3fv(vertex.coordinates[:3])
        glEnd()

# Função triângulo unitário
def draw_unitTriangle(material):
    #color = (0.6,0,0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, material.k_a_rgb)
    glMaterialfv(GL_FRONT, GL_DIFFUSE, material.k_d_rgb)
    glMaterialfv(GL_FRONT, GL_SPECULAR, material.k_e_rgb)
    glMaterialf(GL_FRONT, GL_SHININESS, material.attenuation)
    
    vertices = (
        (0,0,0),
        (0,0,1),
        (1,0,0),
        (0,1,0)
    )

    faces = (
        (0,1,3),
        (0,3,2),
        (0,2,1),
        (1,2,3)
    )


    glBegin(GL_TRIANGLES)
    for face in faces:
        for vertex in face:
            glVertex3fv(vertices[vertex])
    
    glEnd()
    
   

def converte(valor):
    return int(valor[0:valor.find('/')])

def objeto(path, cor=None):
    if cor is None: 
        cor = (0.6, 0.6, 0.6)
    
    vertices = []
    faces_triangulares = []
    faces_quadriculares = []

    with open(path) as meu_arquivo:
        
        for linha in meu_arquivo:
            valores = linha.split()

            if len(valores) == 4 and valores[0] == 'v':
                vertices.append((float(valores[1]), float(valores[2]), float(valores[3])))
            
            elif len(valores) == 4 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                faces_triangulares.append((v1, v2, v3))

            elif len(valores) == 5 and valores[0] == 'f':
                v1 = converte(valores[1]) - 1
                v2 = converte(valores[2]) - 1
                v3 = converte(valores[3]) - 1
                v4 = converte(valores[4]) - 1
                faces_quadriculares.append((v1, v2, v3, v4))

    vertices = tuple(vertices)
    faces_triangulares = tuple(faces_triangulares)
    faces_quadriculares = tuple(faces_quadriculares)

    glBegin(GL_TRIANGLES)
    for face in faces_triangulares:
        #glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
    
    glBegin(GL_QUADS)
    for face in faces_quadriculares:
        #glColor3fv(cor)
        for vertice in face:
            glVertex3fv(vertices[vertice])
    glEnd()
