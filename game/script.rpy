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

transform fade_out:
  alpha 1.0
  linear 0.5 alpha 0.0

transform fade_in:
  alpha 0.0
  linear 0.5 alpha 1.0

transform richard_collapsed_zoom:
  zoom 0.45
  center

transform zoom_upwards_to_half:
  zoom 0.40
  xalign 0.5
  yalign 1.5
  linear 20.0 zoom 0.45

transform zoom_centered_to_half:
  zoom 0.42
  xalign 0.5
  yalign 0.5
  linear 30.0 zoom 0.50

transform carys_neutral_zoom_out:
  zoom 0.55
  linear 2.0 zoom 0.40

transform center_to_left:
   zoom 0.40
   center
   easein 1.0 xalign 0.1

transform left_to_center:
   zoom 0.40
   xalign 0.1
   easein 1.0 center

transform right_to_center:
  zoom 0.40
  xalign 1.0
  easein 1.0 center

transform norm_center:
  zoom 0.40
  center

transform norm_left:
  zoom 0.40
  left

transform norm_right:
  zoom 0.40
  right

transform come_in_from_left:
   zoom 0.40
   xalign -0.5
   yalign 1.0
   easein 1.0 xalign 0.0

transform move_out_from_left:
  zoom 0.40
  xalign 0.0
  yalign 1.0
  easein 1.0 xalign -0.6

transform come_in_from_right:
   zoom 0.40
   xalign 1.3
   yalign 1.0
   easein 1.0 xalign 1.0


 # Show a background. This uses a placeholder by default, but you can
#     # add a file (named either "bg room.png" or "bg room.jpg") to the
#     # images directory to show it.
#
#     scene bg ring with fade
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

# The game starts here.
label start:
#     scene bg meditate
#     show carys meditating at zoom_centered_to_half
#
#     Carys "Stay in the here and now."
#
#     Carys "Listen to the thrum of the city, around but apart."
#
#     Carys "Listen to each step, each clang, each murmur, each rustle. {w}And leave them there."
#
#     Carys "Listen, listen –"
#
#     Carys "Listen – {w} there's someone else?"
#
#     Carys "I don't want someone else."
#
#     Carys "I wanted to get away from the other worlds."
#
#     scene bg busstop left with fade
#
#     show carys neutral at center, carys_neutral_zoom_out
#
#     Carys "{i}Oh god. Someone's actually here.{/i}"
#
#     show carys neutral at center_to_left
#     show gwen smiling at come_in_from_right
#
#     Gwen "Hiya!"
#
#     Carys "Hey."
#
#     Gwen "You taking the 3 bus?"
#
#     Carys "Yeah."
#
#     Gwen "Same."
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Gwen "You been waiting here long?"
#
#     Carys "Yeah."
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Gwen "Gonna be a while. Like, fifteen, twenty minutes."
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Gwen "Wait, aren't you...{w} That boxing girl?"
#
#     Carys "{i}Oh Christ. She knows.{/i}"
#
#     narrator "{cps=6}• • •{/cps}"
#
#     Gwen "Right, right? There was that news story, where, uh..."
#
#     Carys "{i}Just give it a few more seconds...{/i}"
#
#     show gwen at fade_out
#     pause 0.5
#     show gwen shocked at fade_in
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
#
#     scene bg arena with wiperight
#
#     Carys "It was January, after the first snow."
#
#     scene bg locker with wiperight
#
#     show carys neutral at come_in_from_left
#
#     Carys "My debut night. After a year of training, a real match in a real arena."
#
#     Carys "An easy win, they said. Against some hotshot influencer kid trying to put out another stunt video: “I made my boxing debut in 7 days.”"
#
#     show gwen neutral at come_in_from_right
#
#     Gwen "Ain't nothing wrong with that. People gotta hustle."
#
#     Carys "That's not how it works here, in this city. Can't jump the line. Skip the training. Ignore the connections."
#
#     Gwen "Well, he got in somehow. And he got to face you."
#
#     Carys "The organizers are...practical people. They will cut a good deal."
#
#     Gwen "So you did things the long way."
#
#     Carys "I worked for this. He wasn't supposed to come in like this. Not on my debut."
#
#     Gwen "Yeah, I feel that. They played you for some cash."
#
#     Carys "I was lucky to be given a spot. I just wish it was like everyone else's. But I wasn't going to complain."
#
#     Gwen "Sure, don't gotta make nobody mad."
#
#     Carys "Exactly. By the book. The right way, to keep everyone happy."
#
#     Carys "We met, before the round. As is tradition."
#
#     scene bg locker past with pixellate
#
#     show carys boxing at come_in_from_left
#     show richard smiling at come_in_from_right
#
#     Richard "Hey guys, my name's Richard and my team's really glad to be working with you today."
#
#     Carys "Nice to meet you, Richard."
#
#     Richard "So listen, we're recording intros and it'd be really cool if you could give the fans a shoutout, whaddaya say?"
#
#     Carys "No thanks, I'm good. I have to warm up."
#
#     Richard "C'mon! They're going to love it."
#
#     Carys "I think I'll still have to pass."
#
#     Richard "Uh-huh, uh-huh. I see, playing hard to get."
#
#     Richard "Okay, so I don't usually do this, since I'm not sure how great a fit your content is for my channel."
#
#     Richard "But here – I'll also tag your stream in the video description. Just have to say hi!"
#
#     Carys "Richard. I'm just here for the match. I'm not even on social media, okay? Just let it go."
#
#     Richard "Woah there, okay, chill out. I'm just asking. We cool here?"
#
#     Carys "Yeah, all good. You feeling ready?"
#
#     Richard "Ready as I'll ever be. How long did you train for this?"
#
#     Carys "About a year."
#
#     Richard "Hah, you got me beat there! This is day 5 for me. Anyway, I gotta run. Catch you outside."
#
#     Carys "Good luck, Richard."
#
#     show carys boxing at move_out_from_left
#     show richard smiling at right_to_center
#
#     Richard "Okay, we rolling for the intro?"
#
#     Richard "What's up, guys? I'm here at the Bacchus Arena getting ready for the match of a {i}lifetime{/i}!"
#
#     Richard "One week, eight hours of training each day, and what you have is a boxing {i}machine{/i}."
#
#     Richard "And that lady over there? The challenger. She's going {i}down{/i} tonight. Gonna wipe the floor with her {i}so hard{/i}."
#
#     Richard "Like and subscribe, guys, and see you in the ring!"
#
#     scene bg locker with pixellate
#
#     show carys neutral at come_in_from_left
#     show gwen neutral at come_in_from_right
#
#     Carys "He's a different person when the cameras come on."
#
#     Gwen "Ain't that the truth for all of us."
#
#     Carys "All he cares about is what the viewers will think. {w}I saw him trembling. He was afraid."
#
#     Gwen "Poor kid."
#
#     Carys "He's an adult who can make his own decisions. He wanted to be here."
#
#     Carys "I do my warmups. I do my breathing exercises. I go out into the ring."
#
#     scene bg ring with wiperight
#
#     show carys neutral at center, carys_neutral_zoom_out
#
#     Carys "This is the ring, the sacred space. The boxing ring.{w} My boxing ring."
#
#     Carys "I face Richard here. It's all on video. {w}But a video is just appearance."
# #
#     scene bg ring past with pixellate
#
#     show carys boxing at come_in_from_left
#     show richard boxing at come_in_from_right
#
#     Carys "The crowd cheers. For me, taking on an undeserving upstart? For him, daring to try?"
#
#     Carys "He is undisciplined and careless. He doesn't perform well."
#
#     Carys "The crowd jeers. For me, accepting this unworthy debut?"
#
#     Carys "It must be on me. I try harder to please them. I surge forward with more fury."
#
#     show carys punching
#
#     Carys "Round after round he goes down in front of the cameras."
#
#     Carys "And then at last he stays down."
# #
#     show richard boxing at fade_out
#     pause 1.0
#     hide richard
#
#     show carys punching at left_to_center
#     pause 1.0
#     show carys punching at fade_out
#     pause 1.0
#     show carys victorious at fade_in
#
#     Carys "The crowd goes wild. Of course they know who he is, how he has gotten here."
#
#     Carys "I've done my part. I have them on my side. I think it's time to go home."
#
#     scene bg ring with pixellate
#
#     show carys neutral at norm_left
#     show gwen neutral at norm_right
#
#     Gwen "For real?"
#
#     Carys "It's the truth. I should have gone home, but I didn't. {w}I was ready to leave. I wanted to leave."
#
#     scene bg ring past with pixellate
#
#     show carys victorious at norm_center
#
#     Carys "But I want the applause. The praise and glory wrap me in their embrace."
#
#     Carys "That's right, people! Give it up for this wonder of the world."
#
#     Carys "What new spectacle, gentlehuman?"
#
#     Carys "Then I hear think I hear the crowd chanting. In that terrible din I try to make out the words."
#
#     Carys "They're saying 'finish him, finish him'."
#
    scene bg ring ropes with wiperight

    show richard collapsed at richard_collapsed_zoom

    Carys "I look down at him, slumped, eyes closed. He is finished, I know. He is done. Done for."

    Carys "But then I cannot hear anything else but this infernal chant."

    Carys "In that moment, surrounded and safe, it felt so right, do you see? The support and love of a crowd is difficult to ignore."

    Carys "I had to give, and they had to take."

    Carys "You've seen this part before. But you have to keep watching, please."

    Carys "I stride up to him."

    Carys "I am rage and righteousness, and I strike."

    show bg avatar rage with fade

    Carys "I clutch my gloved fist in disbelief, fighting against what I am becoming, or have become."

    Carys "Is this my hand, or an instrument of the crowd?"

    Carys "My ears are ringing, and suddenly the chant dissolves."

    Carys "I see through my haze a vision of a match in honor, among equals. And glory, applause for skill and finesse, not out of reach yet, surely not."

    Carys "I take a sharp breath and my curled fist goes limp."

    scene bg busstop left with pixellate

    show carys neutral at norm_left
    show gwen neutral at norm_right

    Carys "He goes still. The lights come on. The crowd is quiet. Security removes me."

    return


