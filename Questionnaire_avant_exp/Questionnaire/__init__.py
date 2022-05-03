from otree.api import *

import random

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'Questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

     Num = models.StringField()

###################################### Questions personnelles et ID#####

     Pers_2 = models.StringField(
        label = '''
            1. Votre âge :''',
        choices = [['18 ans - 21 ans ','18 ans - 21 ans'],[ '22 ans - 25 ans', '22 ans - 25 ans'],['26 ans - 29 ans','26 ans - 29 ans']],
        widget=widgets.RadioSelectHorizontal,
     )
     Pers_3 = models.StringField(
        label = '''
            2. Votre genre (Pour des raisons liées à l'anonymat, il ne vous est pas demandé de préciser votre genre si autre): 
            ''',
        choices = [['Femme','Femme'],[ 'Homme', 'Homme'], ['Autre','Autre']],
        widget=widgets.RadioSelectHorizontal,
     )
     Pers_4 = models.StringField(
         label='''
           3. Niveau d'éducation (Si vous êtes en L1, L2, cocher le niveau "BAC". Si vous êtes en L3, cocher le niveau "BAC+2"...): 
             ''',
         choices= [['CAP', 'CAP'], ['BAC', 'BAC'], ['BAC+2', 'BAC+2'], ['BAC+3', 'BAC+3'], ['BAC+5', 'BAC+5'], ['BAC+8', 'BAC+8'],['Autre', 'Autre']],
         widget=widgets.RadioSelectHorizontal,
     )
     Pers_5 = models.StringField(
         label='''
           4. Champ disciplinaire principal des études que vous avez faites ou que vous faites actuellement :  
             ''',
         choices = [['Biologie, Santé, Sport','Biologie, Santé, Sport'], ['Droit, Science Politique, Economie et Gestion','Droit, Science Politique, Economie et Gestion',],
                    ['Education, Enseignement, Formation','Education, Enseignement, Formation'], ['Lettres, Langues, Arts et Communication','Lettres, Langues, Arts et Communication'],
                    ['Sciences, Ingénierie, Technologie, Environnement', 'Sciences, Ingénierie, Technologie, Environnement'], ['Sciences Humaines et Sociales','Sciences Humaines et Sociales']],
         widget=widgets.RadioSelect,
     )

################################# The Negative Attitudes towards Robots Scale #####

     NARS_1 = models.StringField(
         label= ''' 
            1. Je ne me sentirais pas à l’aise si les robots éprouvaient des émotions.
            ''',
         choices=[["Fortement en désaccord",
                  "Fortement en désaccord"],
                 ["En désaccord", "En désaccord"],
                 ["Indécis", "Indécis"],
                  ["En accord","En accord"],
                  ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_2 = models.StringField(
         label= ''' 
            2. Des choses graves surviendraient si les robots étaient conçus comme des êtres vivants.
            ''',
         choices=[["Fortement en désaccord",
                  "Fortement en désaccord"],
                 ["En désaccord", "En désaccord"],
                 ["Indécis", "Indécis"],
                  ["En accord","En accord"],
                  ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_3 = models.StringField(
         label= ''' 
            3. Je me sentirais détendu de discuter avec des robots.
            ''',
         choices=[["Fortement en désaccord",
                  "Fortement en désaccord"],
                 ["En désaccord", "En désaccord"],
                 ["Indécis", "Indécis"],
                  ["En accord","En accord"],
                  ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_4  = models.StringField(
         label= ''' 
            4. Je me sentirais mal à l’aise si on me donnait à réaliser une activité dans laquelle je dois utiliser un robot.
            ''',
         choices=[["Fortement en désaccord",
                  "Fortement en désaccord"],
                 ["En désaccord", "En désaccord"],
                 ["Indécis", "Indécis"],
                  ["En accord","En accord"],
                  ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_5  = models.StringField(
         label= ''' 
            5. Si les robots avaient des émotions, je serai capable de devenir ami avec eux.
            ''',
         choices=[["Fortement en désaccord",
                  "Fortement en désaccord"],
                 ["En désaccord", "En désaccord"],
                 ["Indécis", "Indécis"],
                  ["En accord","En accord"],
                  ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_6  = models.StringField(
         label= ''' 
            6. Je serai rassuré si les robots éprouvaient des émotions.
            ''',
         choices=[["Fortement en désaccord",
                  "Fortement en désaccord"],
                 ["En désaccord", "En désaccord"],
                 ["Indécis", "Indécis"],
                  ["En accord","En accord"],
                  ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     NARS_7 = models.StringField(
        label=''' 
            7. Le mot « robot » n’évoque rien pour moi.
            ''',
        choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )

     NARS_8 = models.StringField(
        label=''' 
            8. Je me sentirais nerveux si je devais utiliser un robot devant d’autres personnes.
            ''',
        choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )
     NARS_9 = models.StringField(
         label= '''
            9. Je déteste l’idée selon laquelle des robots puissent émettre des jugements à propos de choses.
            ''',
         choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_10 = models.StringField(
         label='''
            10. Je me sentirais nerveux si je devais simplement rester debout face à un robot.
            ''',
         choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_11 = models.StringField(
         label='''
            11. Je pense que si je dépendais trop des robots, des choses mauvaises pourraient se produire. 
            ''',
         choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     NARS_12 = models.StringField(
         label='''
            12. Je me sentirai très mal à l’aise de devoir parler à un robot. 
            ''',
         choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     NARS_13 = models.StringField(
        label='''
            13. Je crains que les robots aient une mauvaise influence sur les enfants. 
            ''',
        choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )
     NARS_14 = models.StringField(
        label='''
                14. Je pense que, dans le futur, la société sera dominée par les robots.
            ''',
        choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )
     NARS_15 = models.StringField(
        label='''
                15. Je pense que, dans le futur, les robots seront partout dans la société.
            ''',
        choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )
     NARS_16=models.StringField(
             label='''
           16. Je pense que je pourrais me faire des amis avec les robots.
                ''',
             choices=[["Fortement en désaccord",
                       "Fortement en désaccord"],
                      ["En désaccord", "En désaccord"],
                      ["Indécis", "Indécis"],
                      ["En accord", "En accord"],
                      ["Fortement en accord", "Fortement en accord"]],
             widget=widgets.RadioSelectHorizontal,
     )

     NARS_17 = models.StringField(
         label='''
             17. Je me sens rassuré d’être avec des robots.
           ''',
         choices=[["Fortement en désaccord",
              "Fortement en désaccord"],
             ["En désaccord", "En désaccord"],
             ["Indécis", "Indécis"],
             ["En accord", "En accord"],
             ["Fortement en accord", "Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

###################################### TAM2:

     TAM_1 = models.StringField(
        label='''
                1. Si j’ai accès à un algorithme, j’ai l’intention de l’utiliser.
            ''',
        choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             [ "(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )
     TAM_2 = models.StringField(
        label='''
                11. Etant donné que j’ai accès à un algorithme, je prévois de l’utiliser.
            ''',
        choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             [ "(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )

     TAM_3 = models.StringField(
        label='''
                2. L’utilisation d’un algorithme va me permettre d’accomplir mon travail plus rapidement.
            ''',
        choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             [ "(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )


     TAM_4 = models.StringField(
         label='''
           12. L’utilisation d’un algorithme peut améliorer ma performance au travail.

              ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_5 = models.StringField(
          label='''
           3. L’utilisation d’un algorithme peut augmenter ma productivité.
       ''',
          choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
          widget=widgets.RadioSelectHorizontal,
     )

     TAM_6 = models.StringField(
         label='''
           13. Je trouve que l’e-formation est utile pour mon travail.

       ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_7 = models.StringField(
         label='''
           4. Mon interaction avec un algorithme sera clair et compréhensible.
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     TAM_8 = models.StringField(
         label='''
           14. Interagir avec un algorithme ne me demande pas un effort mental conséquent. 
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_9 = models.StringField(
         label='''
           5.  Apprendre à utiliser un algorithme sera facile pour moi.

             ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_10 = models.StringField(
         label='''
             15. Il sera facile pour moi de devenir compétent dans l’utilisation d’un algorithme.

         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_11 = models.StringField(
         label='''
         6. Les personnes qui m’influencent pensent qu’il faut que j’utilise un algorithme.
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_12 = models.StringField(
         label='''
          16. Les personnes qui sont importantes pour moi pensent que je dois utiliser un algorithme.     
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )


     TAM_13 = models.StringField(
         label='''
           7. J’utilise volontairement un algorithme. 
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_14 = models.StringField(
         label='''
           17. Personne ne m’oblige à utiliser un algorithme. 
            ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_15 = models.StringField(
         label='''
           8. Bien que ça peut être utile, personne ne m’oblige à utiliser un algorithme dans mon domaine. 
          ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_16 = models.StringField(
         label='''
         18. Dans mon domaine, les personnes qui utilisent un algorithme ont plus de prestige que ceux qui n’en utilisent pas.
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_17 = models.StringField(
         label='''
          9. Les personnes qui utilisent un algorithme dans mon domaine ont une bonne image.
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_18 = models.StringField(
         label='''
            19. le fait d’utiliser un algorithme est professionnellement valorisant.
          ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_19 = models.StringField(
         label='''
            10 . L’utilisation d’un algorithme est importante pour mon travail. 
            ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     TAM_20 = models.StringField(
         label='''
             20. L’utilisation d’un algorithme est adaptée à la nature de mon travail.
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_21 = models.StringField(
         label='''
             26. L’algorithme produit de bons résultats. 
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     TAM_22 = models.StringField(
         label='''
             22. Je n’ai aucun problème avec la qualité des prédictions de l’algorithme. 
            ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_23 = models.StringField(
         label='''
         25. Je ne rencontre aucune difficulté à dire aux autres les résultats liés à l’utilisation d’un algorithme. 
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_24 = models.StringField(
         label='''
             23. Je crois que je pourrais communiquer les conséquences de l’utilisation d’un algorithme à d’autres personnes. 
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )


     TAM_25 = models.StringField(
         label='''
         24. Les résultats liés à l’utilisation d’un algorithme sont clairs pour moi. 
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )

     TAM_26 = models.StringField(
         label='''
          21. J’aurais des difficultés à expliquer pourquoi l’utilisation d’un algorithme pourrait ou ne pourrait pas être bénéfique. 
         ''',
         choices=[["(1) Fortement en désaccord", "(1) Fortement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Neutre", "(4) Neutre"],
             ["(5) Légèrement en accord", "(5) Légèrement en accord"],
             ["(6) Relativement en accord", "(6) Relativement en accord"],
             ["(7) Fortement en accord", "(7) Fortement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )


###################################### CROYANCE EN LA CHANCE

     Luck_1 = models.StringField(
        label='''
                1. La chance joue un rôle important dans la vie de chacun. 
            ''',
        choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Légèrement en accord", "(4) Légèrement en accord"],
             ["(5) Relativement en accord", "(5) Relativement en accord"],
             ["(6) Complètement en accord", "(6) Complètement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )
     Luck_2 = models.StringField(
        label='''
                2. Certaines personnes ont généralement de la chance, et d'autres ont de la malchance. 
            ''',
        choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )

     Luck_3 = models.StringField(
        label='''
           3. Je me considère comme une personne chanceuse.  
       ''',
        choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )

     Luck_4 = models.StringField(
         label='''
            4. Je crois en la chance. 
            ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_5 = models.StringField(
         label='''
            5. J'ai souvent l'impression que c'est mon jour de chance. 
            ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_6 = models.StringField(
         label='''
            6. Personne ne peut gagner aux jeux de hasard sur le long terme. 
            ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_7 = models.StringField(
         label='''
            7. J'ai généralement de la chance. 
            ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_8 = models.StringField(
         label='''
            8. J'ai tendance à gagner aux jeux de hasard. 
            ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_9 = models.StringField(
         label='''
            9. C'est une erreur de fonder toutes ses décisions sur la chance que l'on pense avoir.
            ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
                  ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
                  ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
                  ["(4) Légèrement en accord", "(4) Légèrement en accord"],
                  ["(5) Relativement en accord", "(5) Relativement en accord"],
                  ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_10 = models.StringField(
         label='''
                   10. La chance joue en ma faveur. 
              ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Légèrement en accord", "(4) Légèrement en accord"],
             ["(5) Relativement en accord", "(5) Relativement en accord"],
             ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_11 = models.StringField(
         label='''
             11. Cela ne me dérange pas de laisser les choses au hasard parce que je suis une personne chanceuse.  
              ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Légèrement en accord", "(4) Légèrement en accord"],
             ["(5) Relativement en accord", "(5) Relativement en accord"],
             ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_13 = models.StringField(
         label='''
             12. Dans ma vie, les choses que je ne peux pas contrôler ont tendance à aller comme je le veux, parce que je suis chanceux. 
          ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Légèrement en accord", "(4) Légèrement en accord"],
             ["(5) Relativement en accord", "(5) Relativement en accord"],
             ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_14 = models.StringField(
        label='''
                13. Je me considère comme étant malchanceux. 
             ''',
        choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Légèrement en accord", "(4) Légèrement en accord"],
             ["(5) Relativement en accord", "(5) Relativement en accord"],
             ["(6) Complètement en accord", "(6) Complètement en accord"]],
        widget=widgets.RadioSelectHorizontal,
     )
     Luck_15 = models.StringField(
         label='''
              14. La chance existe et elle favorise certaines personnes plutôt que d'autres.
         ''',
         choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Légèrement en accord", "(4) Légèrement en accord"],
             ["(5) Relativement en accord", "(5) Relativement en accord"],
             ["(6) Complètement en accord", "(6) Complètement en accord"]],
         widget=widgets.RadioSelectHorizontal,
     )
     Luck_16 = models.StringField(
         label='''
             15. La chance n'est rien de plus que le hasard. 
         ''',
     choices=[["(1) Complètement en désaccord", "(1) Complètement en désaccord"],
             ["(2) Relativement en désaccord", "(2) Relativement en désaccord"],
             ["(3) Légèrement en désaccord", "(3) Légèrement en désaccord"],
             ["(4) Légèrement en accord", "(4) Légèrement en accord"],
             ["(5) Relativement en accord", "(5) Relativement en accord"],
             ["(6) Complètement en accord", "(6) Complètement en accord"]],
     widget=widgets.RadioSelectHorizontal,
     )

# PAGES
class Inst_1(Page):
    pass

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        Liste = ('1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                 'S','T','U','V','W','X','Y','Z')
        ran = random.choices(Liste, k=7)
        player.Num = "".join(ran)

class QR(Page):
    pass

class Pers(Page):
    form_model = 'player'
    form_fields = ['Pers_2', 'Pers_3', 'Pers_4', 'Pers_5']

class Intro_Quest_LUCK_NARS(Page):
    pass

class LUCK(Page):
    form_model = 'player'
    form_fields = ['Luck_1','Luck_2','Luck_3','Luck_4','Luck_5','Luck_6','Luck_7','Luck_8',
                   'Luck_9','Luck_10','Luck_11','Luck_13','Luck_14','Luck_15','Luck_16']

class NARS(Page):
    form_model = 'player'
    form_fields = ['NARS_1', 'NARS_2', 'NARS_3', 'NARS_4', 'NARS_5', 'NARS_6', 'NARS_7', 'NARS_8', 'NARS_9','NARS_10',
                   'NARS_11', 'NARS_12','NARS_13','NARS_14','NARS_15','NARS_16','NARS_17']

class TAM(Page):
    form_model = 'player'
    form_fields = [ 'TAM_1', 'TAM_3', 'TAM_5', 'TAM_7','TAM_9', 'TAM_11', 'TAM_13', 'TAM_15', 'TAM_17', 'TAM_19',
                    'TAM_2', 'TAM_4','TAM_6', 'TAM_8', 'TAM_10', 'TAM_12', 'TAM_14', 'TAM_16', 'TAM_18', 'TAM_20',
                    'TAM_26', 'TAM_22', 'TAM_24', 'TAM_25', 'TAM_23', 'TAM_21']

############################################## RISK GAME ##############################################


class Fin_1(Page):
    pass


page_sequence = [Inst_1, QR,  Pers, Intro_Quest_LUCK_NARS, LUCK, NARS, TAM, Fin_1]

