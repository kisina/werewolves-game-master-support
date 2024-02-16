class Role:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"

    def action_de_nuit(self, tour):
        pass

    def action_de_jour(self, tour, target_player):
        pass

    def get_status(self):
        return f"{self.name} {'is' if self.is_alive else 'was'} {'alive' if self.is_alive else 'dead'}"


class LoupGarou(Role):
    def __init__(self):
        role_description = """Chaque nuit, ils dévorent un Villageois.
Le jour, ils essaient de masquer leur identité nocturne pour échapper à la vindicte populaire.
Ils sont 1, 2, 3 ou 4 suivant le nombre de joueurs et les variantes appliquées.
(En aucun cas un Loup-Garou ne peut dévorer un Loup-Garou)."""
        super().__init__("Loup-Garou", role_description)

    def action_de_nuit(self, tour):
        # Logique spécifique à l'action de nuit du Loup-Garou
        pass


class Villageois(Role):
    def __init__(self):
        role_description = "Il n’a aucune compétence particulière.\r\nSes seules armes sont la capacité d’analyse des comportements pour identifier les Loups-Garous, et la force de conviction pour empêcher l’exécution de l’innocent qu’il est."
        super().__init__("Villageois", role_description)


class Voyante(Role):
    def __init__(self):
        role_description = "Chaque nuit, elle découvre la vraie personnalité d’un joueur de son choix.\r\nElle doit aider les autres Villageois, mais rester discrète pour ne pas être démasquée par les Loups-Garous."
        super().__init__("Voyante", role_description)
    
    def action_de_nuit(self, tour, target_player):
        return "la Voyante se réveille, et désigne un joueur dont elle veut sonder la véritable personnalité !"


class Chasseur(Role):
    def __init__(self):
        role_description = "S’il se fait dévorer par les Loups-Garous ou exécuter malencontreusement par les joueurs, le Chasseur doit répliquer avant de rendre l’âme, en éliminant immédiatement n’importe quel autre joueur de son choix."
        super().__init__("Chasseur", role_description)
        self.was_alive = True
    
    def action_de_jour(self, tour, target_player):
        if self.was_alive == True:
            return "Le chasseur a été tué, il doit éliminer immédiatement un autre joueur de son choix."
        else:
            pass


class Cupidon(Role):
    def __init__(self):
        role_description = "En décochant ses célèbres flèches magiques, Cupidon a le pouvoir de rendre 2 personnes amoureuses à jamais. La première nuit (tour préliminaire), il désigne les 2 joueurs (ou joueuses ou 1 joueur et 1 joueuse) amoureux. Cupidon peut, s’il le veut, se désigner comme l’un des deux Amoureux."
        super().__init__("Cupidon", role_description)

    def definir_les_amoureux(joueur_a, joueur_b):
        joueur_a.amoureux(joueur_b)
        joueur_b.amoureux(joueur_a)

    def action_de_nuit(self, tour, target_player):
        if tour == 1:
            return "Cupidon se réveille !” Cupidon ouvre les yeux et désigne deux joueurs (dont éventuellement lui-même).\r\nLe meneur fait le tour de la table et touche discrètement le dos des deux Amoureux. Le meneur dit : Cupidon se rendort. Cupidon referme les yeux.\r\nLe meneur dit “les Amoureux se réveillent, se reconnaissent, et se rendorment !” Ils ne se montrent pas leur carte de sorte que chacun ignore la véritable personnalité de l’être aimé. Puis le meneur suit le tour normal."
        else:
            pass


class Sorciere(Role):
    def __init__(self):
        role_description = """Elle sait concocter 2 potions extrêmement puissantes :
une potion de guérison, pour ressusciter le joueur tué par les Loups-Garous, une potion d’empoisonnement, utilisée la nuit pour éliminer un joueur.
La Sorcière doit utiliser chaque potion 1 seule fois dans la partie. Elle peut se servir des ses 2 potions la même nuit.
Le matin suivant l’usage de ce pouvoir, il pourra donc y avoir soit 0 mort, 1 mort ou 2 morts.
La Sorcière peut utiliser les potions à son profit, et donc se guérir elle-même si elle vient d’être attaquée par les Loups-Garous."""
        super().__init__("Sorciere", role_description)
        self.a_une_potion_de_guerison = True
        self.a_potion_de_empoisonnement = True

    def action_de_nuit(self, tour, target_player):
        if self.a_une_potion_de_guerison:
            return "Sorcière, veux-tu utiliser la potion de guérison ?"
        if self.a_potion_de_empoisonnement:
            return "Sorcière, veux-tu utiliser la potion d'empoisonnement ?"


class PetiteFille(Role):
    def __init__(self):
        role_description = """La Petite Fille peut, en entrouvrant les yeux, espionner les Loups-Garous pendant leur réveil. Si elle se fait surprendre par un des Loups-Garous, elle meurt immédiatement (en silence), à la place de
la victime désignée.
La Petite Fille ne peut espionner que la nuit, durant le tour d’éveil des Loups-Garous.
Elle n’a pas le droit de se faire passer pour un Loup-Garou et d’ouvrir grand les yeux."""
        super().__init__("Petite Fille", role_description)

    def action_de_nuit(self, tour, target_player):
        if tour > 1:
            return """La Petite Fille ne peut espionner que la nuit, durant le tour d’éveil des Loups-Garous. Elle n’a pas le droit de se faire passer pour un Loup-Garou et d’ouvrir grand les yeux."""
        else:
            pass


class Voleur(Role):
    def __init__(self):
        role_description = """Si on veut jouer le Voleur, il faut ajouter deux cartes Simples Villageois en plus de toutes celles déjà choisies.
Après la distribution, les deux cartes non distribuées sont placées au centre de la table faces cachées.
La première nuit, le Voleur pourra prendre connaissance de ces deux cartes, et échanger sa carte contre une des deux autres.
Si ces cartes sont deux Loups-Garous, il est obligé d’échanger sa carte contre un des deux Loups-Garous.
Il jouera désormais ce personnage jusqu’à la fin de la partie."""
        super().__init__("Voleur", role_description)

    def action_de_nuit(self, tour, target_player):
        if tour == 1:
            return """Le meneur dit “le Voleur se réveille !” Le joueur qui possède la carte Voleur ouvre les yeux et regarde discrètement les deux cartes cachées au milieu, puis change éventuellement de personnage. Le meneur dit “Le Voleur se rendort”. Le Voleur referme les yeux."""
        else:
            pass


class Joueur:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.is_maire = False
        self.est_amoureux = False
        self.is_alive = True

    def __str__(self):
        return f"{self.name} - {str(self.role)}"
    
    def meurt(self):
        self.is_alive = False
    
    def ressuscite(self):
        self.is_alive = True
    
    def amoureux(self, joueur_amoureux):
        self.amoureux = joueur_amoureux
        self.est_amoureux = True
        return(f"{self.name} est amoureux de {joueur_amoureux.name}")


class Partie:
    def __init__(self, players):
        self.players = players
        self.turn_manager = GestionnairePartie(players)

    def start_game(self):
        print("Le jeu commence!")

    def end_game(self):
        print("Le jeu est terminé!")


class GestionnairePartie:
    def __init__(self, players):
        self.players = players
        self.current_player_index = 0
        self.tour = 0
        self.roles = {"Loup-Garou": [],
                      "Villageois": [],
                      "Voyante": [],
                      "Chasseur": [],
                      "Cupidon": [],
                      "Sorciere": [],
                      "Petite Fille": [],
                      "Voleur": []}
        
        for joueur in players:
            self.roles[joueur.role.name].append(joueur.name)
        print(self.roles)


    def next_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"C'est le tour de {current_player.name} ({current_player.role.name}).")

        # Logique du tour, par exemple, appeler les méthodes perform_night_action ou perform_day_action

        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def verifier_condition_de_victoire(self):
        victoire = False
        msg = []
        # Verficiation si les loups-garous ont gagnée
        if all([joueur.role.name=="Loup-Garou" for joueur in self.joueurs_vivants()]):
            victoire = True
            msg.append("Les Loups-Garous ont gagné !")
        if not(any([joueur.role.name=="Loup-Garou" for joueur in self.joueurs_vivants()])):
            victoire = True
            msg.append("Les Villageois ont gagné !")
        if all([joueur.est_amoureux for joueur in self.joueurs_vivants()]):
            victoire = True
            msg.append("Les amoureux ont gagné !")
        
        if msg == []:
            msg.append("Pas de victoire pour l'instant...")

        if victoire:
            return (True, msg)
        else:
            return (False, msg)

    def joueurs_vivants(self):
        return [joueur for joueur in self.players if joueur.is_alive]
    
    def joueurs_amoureux(self):
        return [joueur for joueur in self.players if (joueur.role.is_alive and joueur.est_amoureux)]


"""
def creation_des_joueurs():
    def __init__(self):
        self.list_roles = {'Loup-Garou':4, 'Villageois':13, 'Voyante':1, 'Voleur':1, 'Cupidon':1, 'Chasseur':1, 'Cupidon':1, 'Petite Fille':1}
    
    def ajouter_un_joueur(self):
        nom = input("Quel est le nom du joueur ?")

        joueur1 = Joueur(nom,)
"""


# Exemple d'utilisation
if __name__ == "__main__":
    # Création des joueurs
    joueur1 = Joueur("Joueur 1", LoupGarou())
    joueur2 = Joueur("Joueur 2", Villageois())
    joueur3 = Joueur("Joueur 3", Voyante())
    joueur4 = Joueur("Joueur 4", Chasseur())
    joueur5 = Joueur("Joueur 5", Cupidon())
    joueur6 = Joueur("Joueur 6", Sorciere())
    joueur7 = Joueur("Joueur 7", PetiteFille())
    joueur8 = Joueur("Joueur 8", Voleur())
    joueur9 = Joueur("Joueur 9", LoupGarou())

    liste_joueurs = [
        joueur1,
        joueur2,
        joueur3,
        joueur4,
        joueur5,
        joueur6,
        joueur7,
        joueur8,
        joueur9],

    #for joueur in liste_joueurs:
        #print(f"{joueur.name} - {joueur.role.name} - Est vivant: {joueur.is_alive}")
        #print(f"{joueur.name}")

    # Initialisation du jeu
    jeu = Partie(liste_joueurs)
    jeu.start_game()

    # Gestion des tours
    for _ in range(5):
        jeu.turn_manager.next_turn()


    
    
    a,b = jeu.turn_manager.verifier_condition_de_victoire()
    print(b)

    print("Les joueurs vivants sont:")
    liste_test = jeu.turn_manager.joueurs_vivants()
    print([joueur.name for joueur in liste_test])
    
    print("Les joueurs vivants sont:")
    joueur3.meurt()
    liste_test = jeu.turn_manager.joueurs_vivants()
    print([joueur.name for joueur in liste_test])

    # Fin du jeu
    jeu.end_game()
