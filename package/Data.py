from tinydb import TinyDB, Query


class Data:
    
    def __init__(self, user):
        self.user = user
        self.datas = {}
        self.data = self.user.get_data()
        self.datas['user_data'] = self.data
        self.imc_sante()
    
    
    def imc_sante(self):
        self.datas["imc"] = round(self.data["poids"]/self.data['taille']**2, 2)
        status = self.get_sante_status()
        self.datas['sante']= status
    
    def get_sante(self):
        db = TinyDB("./Data/sante.json")
        query = Query()
        
        sante = db.get(query.id==self.datas['sante'])
        
        return sante

    
    
    def get_sante_status(self):
        classe_sante = None
        if self.get_imc() < 18.5:
            classe_sante = 1
        elif 18.5<=self.get_imc()<25:
            classe_sante = 0
        elif 25<=self.get_imc()<30:
            classe_sante = 2
        elif 30<=self.get_imc()<35:
            classe_sante = 3
        elif 35<=self.get_imc()<40:
            classe_sante = 4
        else:
            classe_sante = 5 
        return classe_sante           
    
    
    def get_imc(self):
        return self.datas['imc']
    
    
    def update(self):
        db = TinyDB("./Data/datas.json")
        user = Query()
        if(len(db.search(user.user_data.pseudo == self.data['pseudo']))==0):
            db.insert(self.datas)
            return
        db.update(self.datas, user.user_data.pseudo==self.data['pseudo'])
        
    @classmethod
    def get_user(cls, pseudo, mdp):
        db = TinyDB("./Data/datas.json")
        user = Query()
        try:
            user=db.search(user.user_data.pseudo==pseudo)[0]
            data = user['user_data']
            if data["mot_de_passe"] == mdp:
                return {'status':True, 'data':data, 'msg':"Connexion Reussi"}
            return {'status':False, 'data':{}, 'msg':"Utilisateur non trouvé"}
        except:
            return {'status':False, 'data':{}, 'msg':"Utilisateur non trouvé"}  

if __name__=="__main__":  
    print(Data.get_user("rach", "secret"))