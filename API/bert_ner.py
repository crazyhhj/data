from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline



def get_des_information(content):
    repr(content).replace(f'\n', '')
    tokenizer = AutoTokenizer.from_pretrained("D:/vscodeFile/map/server/API/ner_org")
    model = AutoModelForTokenClassification.from_pretrained("D:/vscodeFile/map/server/API/ner_org")
    nlp = pipeline("ner", model=model, tokenizer=tokenizer)
    ner_results = nlp(content)
    character: list = []
    character_index: list = []

    location: list = []
    location_index: list = []

    organization: list = []
    organization_index: list = []
    for d in ner_results:
        if 'PER' in d['entity']:
            if d['entity'] == 'B-PER':
                character.append(d['word'])
                character_index.append(d['index'])
            else:
                if len(character) > 0:
                    character[-1] = character[-1] + ' ' + d['word']
        if 'LOC' in d['entity']:
            if d['entity'] == 'B-LOC':
                location.append(d['word'])
                location_index.append(d['index'])
            else:
                if len(location) > 0:
                    location[-1] = location[-1] + ' ' + d['word']
        if 'ORG' in d['entity']:
            if d['entity'] == 'B-ORG':
                organization.append(d['word'])
                organization_index.append(d['index'])
            else:
                if len(organization) > 0:
                    organization[-1] = organization[-1] + ' ' + d['word']
    character_set: list = []
    location_set: list = []
    organization_set: list = []
    for i in range(len(character)):
        unit = {'name': character[i], 'index': character_index[i]}
        character_set.append(unit)
    for i in range(len(location)):
        unit = {'name': location[i], 'index': location_index[i]}
        location_set.append(unit)
    for i in range(len(organization)):
        unit = {'name': organization[i], 'index': organization_index[i]}
        organization_set.append(unit)

    character_fre = {}
    for char in character:
        character_fre[f'{char}'] = 0
    for char in character:
        character_fre[f'{char}'] = character_fre[f'{char}'] + 1
    location_fre = {}
    for loc in location:
        location_fre[f'{loc}'] = 0
    for loc in location:
        location_fre[f'{loc}'] = location_fre[f'{loc}'] + 1
    organization_fre = {}
    for org in organization:
        location_fre[f'{org}'] = 0
    for org in organization:
        location_fre[f'{org}'] = location_fre[f'{org}'] + 1
    # print(character_fre, location_fre, organization_fre)
    return {'person': character_set, 'loc': location_set, 'org': organization_set, 'fre': [character_fre, location_fre, organization_fre]}

if __name__ == '__main__':
    example = """
    Once upon a time, in the bustling city of New York, there was a young woman named Samantha. She was a journalist working for the New York Times, one of the most prestigious media organizations in the world.

    One day, Samantha received a call from her editor, James, who told her about a new story he wanted her to cover. It was about a famous celebrity couple, John and Sarah, who were rumored to be getting a divorce. Samantha was thrilled at the opportunity and immediately got to work.

    She spent the next few days investigating and interviewing many people who knew the couple, including their friends, family, and colleagues. She also visited many places associated with the couple, such as their home, their favorite restaurant, and their vacation spot.

    As Samantha dug deeper into the story, she discovered some shocking secrets that were hidden behind the glamorous facade of John and Sarah's public image. She found out that John had been involved in an affair with a woman named Jessica, who was a popular singer and also a close friend of Sarah's.

    Samantha's story quickly gained traction and was soon picked up by other media organizations, including CNN, ABC, and NBC. The news of the celebrity couple's impending divorce caused a sensation among their fans, and many organizations started speculating about the reasons behind it.

    However, not everyone was happy with Samantha's story. Some organizations, including the public relations firm representing John and Sarah, accused Samantha of spreading rumors and falsehoods. They threatened to sue the New York Times and Samantha herself for defamation.

    But Samantha was not deterred. She had done her research and had all the evidence to back up her story. She continued to pursue the truth, even in the face of adversity.

    In the end, Samantha's story won the Pulitzer Prize, one of the most prestigious awards in journalism. It was a testament to her dedication, hard work, and journalistic integrity.

    As for John and Sarah, they eventually got divorced, and their lives were forever changed. But Samantha's story had a lasting impact on the world of journalism, inspiring many young journalists to pursue the truth, no matter what the cost.
    """
    joker_ex = """
    CLOSE ON TV, Murray Franklin is in the middle of doing his
     monologue.

                         MURRAY FRANKLIN (ON TV)
               So I told my youngest son, Tommy,
               remember he's the 'not so bright'
               one,--
                   (laughter)
               I told him that the garbage strike
               is still going on. And he says, and
               I'm not kidding, Tommy says, "So
               where are we gonna get all our
               garbage from?"

     Murray Franklin cracks up at his own joke. Studio audience
     laughs.

     JOKER LAUGHS, LYING IN BED NEXT TO HIS UNCONSCIOUS MOTHER in
     the large overcrowded treatment room.

     Blue curtain dividers separate the bays. He's watching the
     show on a TV bolted high on the wall. He glances over at his
     mother, laughing over the sounds of her labored breath, the
     pain and suffering of those around him.

     He looks back up at the television.

                         MURRAY FRANKLIN (ON TV)
               And finally, in a world where
               everyone thinks they could do my
               job, we got this videotape from the
               Gotham Comedy Club. Here's a guy
               who thinks if you just keep
               laughing, it'll somehow make you
               funny. Check out this joker.
                                                          67.


EXTREME CLOSE ON TV, GRAINY VIDEO OF JOKER'S STAND-UP
PERFORMANCE. Joker on stage smiling behind the microphone,
under the harsh spotlight.

Joker watching himself on TV, his jaw drops--

                     JOKER (ON TV)
              (trying to stop himself
               from laughing)
          -- good evening, hello.
              (deep breath; trying to
               stop laughing)
          Good to be here.
              (keeps cracking up)
          I, I hated school as a kid. But my
          mother would always say,--
              (bad imitation of his mom,
               still laughing)
          "You should enjoy it. One day
          you'll have to work for a living."
              (laughs)
          "No I won't, Ma. I'm gonna be a
          comedian!"

Back to Murray Franklin shaking his head, trying not to
laugh.

                    MURRAY FRANKLIN (ON TV)
          You should have listened to your
          mother.

The studio audience erupts into laughter.

ANGLE ON JOKER, watching Murray Franklin make fun of him on
TV. He gets up and starts walking toward the TV set as if in
a trance. Unsure if this is really happening.

                    MURRAY FRANKLIN (ON TV)
          One more, Bernie. Let's see one
          more. I love this guy.

The tape continues of Joker at the comedy club.

                     JOKER (ON TV)
          It's funny, when I was a little boy
          and told people I wanted to be a
          comedian, everyone laughed at me.
              (opens his arms like a big
               shot)
          Well no one is laughing now.

Dead silence. Nobody is laughing. Not even him.

CUT BACK CLOSE ON MURRAY FRANKLIN, just shaking his head.
                                                              68.


                         MURRAY FRANKLIN (ON TV)
               You can say that again, pal!

     Murray cracks up and the studio audience laughs along with
     him.

     CLOSE ON JOKER, looking up at the television, hearing them
     all laughing at him.

     Beat.

                                                        JUMP CUT:

     Joker is dragging a chair to the television set.

     In a rage, he gets up on the chair and tries to pull the TV
     out of the wall, as the show continues to play--

     But the set is firmly secured to the wall, and Joker pulls so
     hard the chair flips from underneath him and he goes flying
     up the air, crashing down hard onto the floor.
    """
    a = get_des_information(joker_ex)
    print(a)