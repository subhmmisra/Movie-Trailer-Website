import fresh_tomatoes
import media

# Passing arguments to the functions to get variables initilized

# args are title, storyline, poster link, and a trailer link.
conjuring = media.Movie("Conjuring", "A horror story of a mother",
                        "https://goo.gl/3Wu2xM",
                        "https://www.youtube.com/watch?v=k10ETZ41q5o")

superman = media.Movie("Superman", "Origination of superman",
                       'https://upload.wikimedia.org/wikipedia/en/thumb/8/85/'
                       'ManofSteelFinalPoster.jpg/220px-ManofSteelFinalPoster'
                       '.jpg', "https://www.youtube.com/watch?v=T6DJcgm3wNY")

sholay = media.Movie("Sholay", "A street boy", 'http://www.gstatic.com/tv/'
                     'thumb/dvdboxart/71627/p71627_d_v8_aa.jpg',
                     "https://www.youtube.com/watch?v=hLhzpe3_V_g")
slumdog_millionair = media.Movie("Slumdog Millionaire", "boy won the game",
                                 'https://upload.wikimedia.org/wikipedia/en/'
                                 '9/92/Slumdog_Millionaire_poster.png',
                                 "https://www.youtube.com/watch?v=AIzbwV7on6Q")
jthj = media.Movie("JTHJ", "Magicians", 'https://upload.wikimedia.org'
                   '/wikipedia/en/thumb/f/f9/Jab_Tak_Hai_Jaan_Poster.jpg/'
                   '220px-Jab_Tak_Hai_Jaan_Poster.jpg',
                   "https://www.youtube.com/watch?v=v0UXgoJ9Shg")
enthiran = media.Movie("Enthiran", """The story revolves around the struggle of
                       scientist Vaseegaran (played by Rajinikanth) to control
                       his creation, an android named Chitti (also played by
                       Rajinikanth), after Chitti's software is upgraded to
                       give it the ability to comprehend and exhibit human
                       emotions.The project backfires when the robot falls and
                       is manipulated by Bohra (Denzongpa), a rival scientist
                       into becomi""", 'http://t0.gstatic.com/images?q=tbn:'
                       'ANd9GcQLP1c0l7Hg4FQe32YIBoaLGdRDFJm3jI_8leiVqGL7CMT'
                       '2Xh7F', "https://www.youtube.com/watch?v=ODxHJasuCx4")
darr = media.Movie("Darr", "Lovestory of an insane", 'https://upload.wikimedia'
                   '.org/wikipedia/en/3/34/Darr_poster.jpg', 'https://www.'
                   'youtube.com/watch?v=huj9_8uV5y8')
mga = media.Movie("Mughal-E-Azam", "A typical love", 'http://www.gstatic.com/'
                  'tv/thumb/movieposters/31317/p31317_p_v8_aa.jpg',
                  'https://www.youtube.com/watch?v=rXz_vWzMh_U')
tamasha = media.Movie("Tamasha", "An engineer", 'http://t2.gstatic.com/images?'
                      'q=tbn:ANd9GcSk-ArD77KvBAWBVKRULEp53cnr7I7ouYHGrWLzhinpP'
                      'VQxRdvq', 'https://www.youtube.com/watch?v=o-e5eWVCzx8')

# Giving all the variables to a list/array in order to be feteched.
movies = [conjuring, sholay, superman, jthj,
          slumdog_millionair, enthiran, darr, mga, tamasha]
fresh_tomatoes.open_movies_page(movies)
