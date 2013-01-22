# -*- coding: utf-8 -*-

from Oracle import Oracle

class Review(Oracle):
    def __init__(self, review_id = None, usuario_id = None, lbs_id = None, titulo = None, comentario = None, numlikes = None, denuncia = None, comentario_old = None, classificacao = None, *args, **kwargs):
        super(Review, self).__init__(*args, **kwargs)
        self.review_id = review_id
        self.usuario_id = usuario_id
        self.lbs_id = lbs_id
        self.comentario = comentario if classificacao != 'REJECTED' else comentario_old
        self.numLikes = numlikes
        self.titulo = titulo if titulo is not None else ''
        self.denuncia = denuncia if denuncia is not None else 0
        self.comentario_old = comentario_old
        self.classificacao = classificacao
        self.getUserData()
        self.getPoiData()

    def getUserData(self):
        query = "select pois, avaliacoes, fotos, nome from meu_apnt_v6.tbl_usuario where usuario_id = '{usr}'".format(usr = self.usuario_id)
        self.userPois, self.userAvaliacoes, self.userFotos, self.userNome = self.fetchOne(query)

    def getPoiData(self):
        query = """select avaliacoes, rating, up, titulo, descricao,
        (select nome from meu_apnt_v6.tbl_categorias where categoria_id = c.categoria_id),
        (select subnome from meu_apnt_v6.tbl_subcategorias where subcategoria_id = c.subcategoria_id)
        from meu_apnt_v6.tbl_comunidade c where lbs_id = '{poi}'""".format(poi = self.lbs_id)
        self.poiAvaliacoes, self.poiRating, self.poiUp, self.poiTitulo, self.poiDescricao, self.poiCat, self.poiSubCat = self.fetchOne(query)


class MockReview(object):
    def __init__(self, *args, **kwargs):
        super(MockReview, self).__init__(*args, **kwargs)
        self.review_id = 0
        self.usuario_id = 0
        self.lbs_id = '4D68MNVY'
        self.comentario = u"Hotel muito bom, atendimento ótimo, lugar bonito, comida ótima, só é um pouco longe, mas o hotel é maravilhoso..."
        self.numlikes = 5
        self.titulo = u"Hotel nota 10!"
        self.denuncia = 2
        self.comentario_old = ""
        self.classificacao = u"Approved"
        self.getUserData()
        self.getPoiData()

    def getUserData(self):
        self.userPois, self.userAvaliacaoes, self.userFotos = 10, 5, 100
        self.userNome = u"Rutênio de Oliveira César"

    def getPoiData(self):
        self.poiAvaliacoes = 10
        self.poiRating = 1
        self.poiUp = 9
        self.poiTitulo = u"Hotel Quality"
        self.poiDescricao = u"Em meio a uma grande área com piscinas, quadras e um dos melhores fitness center da cidade, o b Quality /b oferece Apartamentos e Suites equipados com internet banda larga."
        self.poiCat = u"Hotéis e Pousadas"
        self.poiSubCat = u"Hospedagem em Geral"
