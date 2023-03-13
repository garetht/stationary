# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Carys = Character("Carys", who_color="#518951")
define Gwen = Character("Gwen", who_color="#b79f01")
define Richard = Character("Richard", who_color="#b79f01")
define Vaughan = Character("Vaughan")
define Bryn = Character("Bryn")

define dots = "{cps=6}• • •{/cps}"

transform bgzoom:
  zoom 0.8

transform zoom_upwards_to_half:
  zoom 0.40
  xalign 0.5
  yalign 1.5
  linear 20.0 zoom 0.45

transform zoom_upwards_to_half_2:
  zoom 0.45
  xalign 0.5
  yalign 1.5
  linear 20.0 zoom 0.50

transform zoom_centered_to_half:
  zoom 0.42
  xalign 0.5
  yalign 0.5
  linear 30.0 zoom 0.50

transform zoom_centered_to_half_2:
   zoom 0.46
   xalign 0.5
   yalign 0.5
   linear 30.0 zoom 0.56

transform unzoom_centered:
   zoom 0.60
   xalign 0.5
   yalign 0.5
   linear 10.0 zoom 0.46

transform carys_neutral_zoom_out:
  zoom 0.55
  linear 2.0 zoom 0.44

transform center_to_left:
   zoom 0.44
   center
   easein 1.0 xalign 0.1

transform come_in_from_left:
   zoom 0.40
   xalign -0.5
   yalign 1.0
   easein 1.0 xalign 0.1

transform come_in_from_right:
   zoom 0.38
   xalign 1.3
   yalign 1.0
   easein 1.0 xalign 1.0


# The game starts here.

label start:

#     scene bg meditate
#
#     show carys meditating at zoom_centered_to_half
#
#     Carys "Stay in the here and now."
#
#     Carys "Listen to the thrum of the city, around but apart."
#
#     Carys "Listen to each step, each clang, each murmur, each rustle. {w}And leave them there."
##
#     Carys "Listen, listen –"
#
#     Carys "Listen – {w} there's someone else?"
#
#     Carys "I don't want someone else."
#
#     Carys "I wanted to get away from the other worlds."
#
#     # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.
#
#     scene bg rink with fade
#
#     # This shows a character sprite. A placeholder is used, but you can
#     # replace it by adding a file named "eileen happy.png" to the images
#     # directory.
#
#     show carys angry boxing at zoom_upwards_to_half
#
#     # These display lines of dialogue.
#
#     Carys "This is the ring, the sacred space. The boxing ring.{w} My boxing ring."
#
#     Carys "Focus is all that matters. Tune the people out."
#
#     Carys "They're here for you, but you're here for yourself."
#
#     Carys "Control the space. If you control the borders, you can let chaos reign inside."
#
#     Carys "Chaos, violence, anger - in the box, it's all a game."
#
#     Carys "But never let it out. {w} I won't let that happen again."
#
#     show carys smug boxing at zoom_upwards_to_half
#
#     Carys "This is the ring, the silly space. The same ring. The circus ring."
#
#     Carys "The one you're in if you don't have control."
#
#     Carys "Big-tent lights and trumpets galore. Where you boast and preen."
#
#     Carys "The crowd wants it all. If you give in they take it all."
#
#     Carys "That's right, people! Give it up for this wonder of the world."
#
#     Carys "What new spectacle, gentlehuman?"
#
#     Carys "What glorious violence can I unleash?"
#
#     show carys angry boxing at zoom_upwards_to_half
#
#     Carys "But no – focus. Focus!"
#
#     Carys "Match is in three weeks. Drills and exercises, remember. No soda. No sweets. Mental and physical mastery. {w}Nothing less."
#
#     Carys "Listen – {w} to the drums?"
#
#     Carys "Get out of my head, Ringo."
#
#     Carys "Back to the real world."

    scene bg busstop left with fade

    show carys neutral at center, carys_neutral_zoom_out

    Carys "{i}Oh great. Someone's here.{/i}"

    show carys neutral at center_to_left
    show gwen smiling at come_in_from_right

    Gwen "Hey you!"

#     Carys "{i}Oh god. Who is it?{/i}"
#
#     Carys "Hey."
#
#     Gwen "You taking the 3 bus?"
#
#     Carys "Yeah."
#
#     Gwen "Same, dude."
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Gwen "You been waiting here long?"
#
#     Carys "Yeah."
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Gwen "Gonna be a while."
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Gwen "Like, fifteen, twenty minutes."
#
#     narrator "{cps=6}• • •{/cps}"

#     Gwen "Wait, aren't you...{w} That boxing girl?"
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Carys "{i}Oh Christ. She knows.{/i}"
#
#     Gwen "Right, right? There was that news story, where, uh..."
#
#     Carys "{i}Just give it a few more seconds.{/i}"
#
#     show gwen shocked
#
#     Gwen "Oh shit. That was you...with the guy and the blood and...what did you do to him?"
#
#     Carys "{i}Here we go again.{/i}"
#
#     Carys "Okay, listen. It isnt't what you think."
#
#     Gwen "No?"
#
#     Carys "No. I'll tell it to you in so much detail you'll think you were there."

    scene bg arena with dissolve

    Carys "It was January, after the first snow."

    scene bg locker with dissolve

    show carys neutral at come_in_from_left

    Carys "It was my debut night. After a year of training, a real match in a real arena."

    Carys "An easy win, they said. Against some hotshot influencer kid trying to put out another stunt video: “I made my boxing debut in 7 days.”"

    show gwen neutral at come_in_from_right

    Gwen "Ain't nothing wrong with that. People gotta hustle."

    Carys "That's not how it works here, in this city. Can't jump the line. Skip the training. Ignore the connections."

    Gwen "Well, he got in somehow. And he got to face you."

    Carys "The organizers are...practical people. They will cut a good deal."

    Gwen "So you did things the long way."

    Carys "The way everyone else does."

    Gwen "Sure, don't gotta make nobody mad."

    Carys "Exactly. By the book. The right way, to keep everyone happy."

    Carys "We met, before the round. As is tradition."

    scene bg locker past with fade

    show carys angry boxing at come_in_from_left

    Richard "Hey guys, my name's Richard and my team's really glad to be working with you today."
    # This ends the game.

    return
