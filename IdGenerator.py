class IdGenrerator:

    idcount = 0
    @staticmethod
    def getId():
        IdGenrerator.idcount+=1
        return IdGenrerator.idcount
