class Role:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_alive = True

    def __str__(self):
        return f"{self.name}: {self.description}"

    def action_de_nuit(self, game):
        pass

    def action_de_jour(self, game, target_player):
        pass

    def get_status(self):
        return f"{self.name} {'is' if self.is_alive else 'was'} {'alive' if self.is_alive else 'dead'}"


class LoupGarou(Role):
    def __init__(self):
        super().__init__("Loup-Garou", "Membre de la meute des Loups-Garous")

    def action_de_nuit(self, game):
        # Logique spécifique à l'action de nuit du Loup-Garou
        pass


class Villageois(Role):
    def __init__(self):
        role_description = "Il n’a aucune compétence particulière.\r\nSes seules armes sont la capacité d’analyse des comportements pour identifier les Loups-Garous, et la force de conviction pour empêcher l’exécution de l’innocent qu’il est."
        super().__init__("Villageois", role_description)

    def action_de_jour(self, game, target_player):
        # Logique spécifique à l'action de jour du Villageois
        pass


class Voyante(Role):
    def __init__(self, name, description):
        role_description = "Chaque nuit, elle découvre la vraie personnalité d’un joueur de son choix.\r\nElle doit aider les autres Villageois, mais rester discrète pour ne pas être démasquée par les Loups-Garous."
        super().__init__("Voyante", role_description)
    
    def action_de_jour(self, game, target_player):
        return "la Voyante se réveille, et désigne un joueur dont elle veut sonder la véritable personnalité !"


class Joueur:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return f"{self.name} - {str(self.role)}"


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

    def next_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"C'est le tour de {current_player.name} ({current_player.role.name}).")

        # Logique du tour, par exemple, appeler les méthodes perform_night_action ou perform_day_action

        self.current_player_index = (self.current_player_index + 1) % len(self.players)


# Exemple d'utilisation
if __name__ == "__main__":
    # Création des joueurs
    loup_garou = LoupGarou()
    villageois = Villageois()
    joueur1 = Joueur("Joueur 1", loup_garou)
    joueur2 = Joueur("Joueur 2", villageois)

    # Initialisation du jeu
    jeu = Partie([joueur1, joueur2])
    jeu.start_game()

    # Gestion des tours
    for _ in range(5):
        jeu.turn_manager.next_turn()

    # Fin du jeu
    jeu.end_game()
