import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "tabulate"])
import subprocess
import sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])
from tabulate import tabulate
import pandas as pd
print("What’s up! Diva Devo here — let’s ride the fashion vibe together!!!!!!")
gender=input("Select your gender(M for Male / F for Female): ")
print('''Select you body type from the given menu:
1)Pear

2)Apple

3)Hourglass

4)Rectangle

5)Inverted Triangle

6)Oval

7)Trapezoid ''')
shape=int(input("enter your body shape number: "))
print("what is your mood today?\n")
a=["SUNNY GLOW MOOD","LOW SOCIAL WEDNESDAY","TANGLED THOUGHTS","SPOTLIGHT DIVA","COFFEE AND RAIN","BLUE HOUR","UNEXPECTED SPARKLE","STORM SURGE"]
b=["Happy Good Vibes","Silent Black Vibes","Anxious Mood","Popular Vibes","Asthetic Mood","Sad Mood","Surprise Me Mood","Angry Furious"]
c=["Bright, Warm","Dark Colours","Muted Tones","Brbie Pallet/Bold Neutrals","Vintage Pallet","Blue Colours","Fluorescent Colours","Yellowish Red"]
title={"Mood":a,"Meaning of Mood":b,"Colour Preferences":c}
df=pd.DataFrame(title,index=[1,2,3,4,5,6,7,8])
print(tabulate(df, headers='keys', tablefmt='grid'))
while True:
    mood=int(input("enter your mood number: "))
    print("Let us see what can you wear today!!!\n")
    if gender=='F':
        if shape==1:
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Bright headband, bold statement earrings, chunky necklace.

                  2)Top – Off-shoulder or puff-sleeve top in sunshine yellow or hot pink.

                  3)Bottom – High-waist wide-leg trousers or A-line skirt in white/pastel.

                  4)Waist – Fun neon or metallic belt to cinch.

                  5)Shoes – Strappy block heels or colourful wedges.

                  6)Bag – Pop-colour crossbody or mini handbag.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek braids or center-parted hair; silver gothic rings, small black studs or cross earrings, maybe a choker.

                  2)Top – Black collared blouse or fitted top with lace/mesh sleeves to draw attention upward.

                  3)Bottom – High-waist A-line skirt or pleated mini in black/dark plaid to balance hips.

                  4)Waist – Slim black belt with subtle silver buckle for definition.

                  5)Shoes – Chunky Mary Janes, lace-up boots, or platform oxfords in black.

                  6)Bag – Structured mini satchel or crossbody in black leather with silver accents.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose low bun or soft waves; delicate studs, thin chain necklace, minimal bracelet.

                  2)Top – Relaxed fit blouse or knit in muted sage, dusty rose, or soft grey to soothe and balance.

                  3)Bottom – High-waist straight trousers or flowy midi skirt in beige, taupe, or muted navy for comfort.

                  4)Waist – Thin neutral belt or leave unbelted for a relaxed silhouette.

                  5)Shoes – Soft leather loafers, ballet flats, or low block heels in nude, grey, or dusty brown.

                  6)Bag – Slouchy tote or crossbody in a muted earthy tone (olive, clay, or sand).''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek ponytail or soft curls; sparkly studs or heart-shaped hoops; dainty layered necklaces in gold/rose-gold.

                  2)Top – Fitted crop top, corset top, or off-shoulder blouse in hot pink, bubblegum, or pastel lavender (adds attention upward).

                  3)Bottom – High-waist A-line mini skirt or wide-leg trousers in white, blush, or pastel blue (balances pear shape).

                  4)Waist – Shiny slim belt or pearl-detailed belt for a chic Barbie vibe.

                  5)Shoes – Platform heels, strappy sandals, or cute sneakers in pink, silver, or white.

                  6)Bag – Mini shoulder bag or sparkly clutch in Barbie pink, glitter silver, or holographic tones.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose waves or messy bun; pearl studs, vintage locket necklace, thin gold rings.

                  2)Top – Puff-sleeve blouse or peter-pan collar shirt in cream, dusty rose, or muted mustard to draw focus upward.

                  3)Bottom – High-waist A-line skirt, culottes, or wide-leg trousers in earthy browns, olive, or burgundy (balances pear shape).

                  4)Waist – Woven or leather belt in tan/caramel for definition.

                  5)Shoes – Vintage-inspired loafers, Mary Janes, or block-heeled boots in muted brown or oxblood.

                  6)Bag – Structured satchel, mini vintage handbag, or crossbody in tan, deep green, or navy.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Jewellery –Loose hair or low ponytail; small silver hoops or simple stud earrings; delicate chain bracelet.

                  2)Top – Cozy oversized knit or flowy blouse in light blue, dusty navy, or slate teal (focus upwards, comforting vibe).

                  3)Bottom – High-waist straight jeans, flowy palazzo pants, or A-line skirt in deeper blue to balance proportions.

                  4)Waist –Soft belt in navy or denim tone, or leave relaxed for comfort.

                  5)Shoes –Comfortable flats, low-top sneakers, or ankle boots in muted blue, grey, or white.

                  6)Bag – Slouchy tote or crossbody in faded denim blue or soft grey.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Jewellery – High ponytail or space buns; neon chunky hoops or acrylic earrings; layered bangles or cuffs.

                  2)Top – Cropped neon hoodie, mesh top, or fitted tank in fluorescent pink, green, or orange to draw the eye upward.

                  3)Bottom – High-waist black wide-leg pants, pleated skirt, or denim with neon side stripes (balances pear shape while letting colours pop).

                  4)Waist – Bright neon belt or chain belt as a fun highlight.

                  5)Shoes – Chunky sneakers or platform sandals in neon mix (pink + green / orange + yellow).

                  6)Bag – Mini backpack or crossbody in transparent neon or holographic finish.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek high ponytail or messy bun; gold hoops or geometric earrings; chunky cuff bracelet.

                  2)Top – Fitted structured blouse or cropped jacket in fiery red, maroon, or mustard-yellow to draw eyes upward.

                  3)Bottom – High-waist black leather pants, dark trousers, or A-line skirt in deep red/oxblood to balance hips.

                  4)Waist – Bold statement belt with gold or metallic buckle for dominance.

                  5)Shoes – Combat boots, block heels, or sharp pointed-toe shoes in red, black, or gold.

                  6)Bag – Structured handbag or crossbody in deep red or mustard with metallic accents. ''')
        elif shape==2:
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Side-parted waves or voluminous curls; chandelier earrings to lift the face.
                  2)Top – Flowing empire-waist blouse in sunshine yellow or coral (draws focus away from midsection).
                  3)Bottom – Straight-leg trousers or tailored skirt in white/pastel for balance.
                  4)Waist – Avoid thick belts; choose soft draping instead.
                  5)Shoes – Wedges or block heels in cheerful tones.
                  6)Bag – Medium crossbody in a pop colour (pink, aqua, lime).''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek straight hair; silver studs or gothic choker.
                  2)Top – Structured dark blouse with V-neck or wrap style to slim the torso.
                  3)Bottom – Black straight trousers or pleated midi skirt for balance.
                  4)Waist – Dark wrap detail instead of a belt.
                  5)Shoes – Platform boots or chunky Mary Janes.
                  6)Bag – Black satchel with silver chain detail.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Low ponytail; minimal studs; slim chain bracelet.
                  2)Top – Relaxed tunic or flowy blouse in muted sage, dusty blue, or soft grey.
                  3)Bottom – Straight trousers or soft palazzos in taupe or muted navy.
                  4)Waist – Skip belts; keep flowy lines for comfort.
                  5)Shoes – Comfortable flats or loafers in muted tones.
                  6)Bag – Slouchy tote in earthy muted colour.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Glossy blowout or ponytail; sparkly studs, layered necklaces.
                  2)Top – Off-shoulder or empire-line blouse in hot pink, bubblegum, or lavender.
                  3)Bottom – Straight trousers or pastel culottes to balance midsection.
                  4)Waist – Avoid bold belts; use vertical seams for slimming.
                  5)Shoes – Cute platform sandals in pastel tones.
                  6)Bag – Barbie-pink clutch or metallic mini handbag.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Soft curls; vintage brooch or pearl studs.
                  2)Top – Empire-waist vintage blouse in cream, mustard, or dusty rose.
                  3)Bottom – Wide-leg trousers or A-line skirt in olive, brown, or burgundy.
                  4)Waist – Draped fabric, no tight belts.
                  5)Shoes – Mary Janes or retro block heels in muted brown.
                  6)Bag – Vintage satchel or structured handbag.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose waves; delicate silver studs or teardrop earrings.
                  2)Top – Oversized cardigan or tunic in slate blue or dusty navy.
                  3)Bottom – Straight jeans or loose trousers in deeper blue.
                  4)Waist – Keep it flowy, no belts.
                  5)Shoes – Soft sneakers or ankle boots in grey/blue.
                  6)Bag – Faded denim crossbody or soft grey tote.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Jewellery – High ponytail; neon acrylic earrings or bangles.
                  2)Top – Neon draped top (pink, orange, or green).
                  3)Bottom – Solid black or denim pants with neon accents.
                  4)Waist – Neon belt or side chain for highlight.
                  5)Shoes – Chunky sneakers or neon sandals.
                  6)Bag – Transparent neon mini backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek bun; bold gold hoops; statement cuff.
                  2)Top – Structured fiery red or mustard wrap blouse to define shoulders.
                  3)Bottom – Black straight trousers or dark skirt.
                  4)Waist – Gold-accented belt (not too wide).
                  5)Shoes – Combat boots or sharp heels in black/red.
                  6)Bag – Red or mustard structured handbag with metallic detail.''')
        elif shape==3:  
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Bouncy curls; colourful hoops.
                  2)Top – Fitted wrap top in bright coral/yellow.
                  3)Bottom – High-waist flared skirt or tailored trousers in white/pastel.
                  4)Waist – Bold belt to highlight curves.
                  5)Shoes – Strappy block heels or wedges.
                  6)Bag – Bright crossbody or mini tote.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek middle part; layered chokers.
                  2)Top – Fitted corset or lace top in black.
                  3)Bottom – High-waist pencil skirt or leather pants.
                  4)Waist – Slim black belt with silver buckle.
                  5)Shoes – Platform boots or chunky Mary Janes.
                  6)Bag – Black structured handbag.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose bun; tiny stud earrings.
                  2)Top – Soft knit wrap top in sage/grey.
                  3)Bottom – High-waist relaxed trousers in muted navy/taupe.
                  4)Waist – Thin neutral belt or none for comfort.
                  5)Shoes – Soft loafers or ballet flats.
                  6)Bag – Slouchy muted tote.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Glossy waves; sparkly studs + layered necklaces.
                  2)Top – Cropped corset or off-shoulder blouse in hot pink/pastel lilac.
                  3)Bottom – High-waist flared mini skirt or pastel wide-leg trousers.
                  4)Waist – Slim pearl/glitter belt.
                  5)Shoes – Platform sandals or Barbie heels.
                  6)Bag – Mini pink clutch or holographic bag.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Soft curls; pearl studs & vintage locket.
                  2)Top – Fitted puff-sleeve blouse in cream/muted rose.
                  3)Bottom – High-waist A-line skirt or culottes in earthy tones.
                  4)Waist – Woven or tan leather belt.
                  5)Shoes – Vintage Mary Janes or block-heeled loafers.
                  6)Bag – Mini satchel or structured handbag.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose waves; delicate silver chain.
                  2)Top – Cozy fitted knit in dusty navy/sky blue.
                  3)Bottom – High-waist jeans or flowy skirt in deeper blue.
                  4)Waist – Relaxed, unbelted for comfort.
                  5)Shoes – Soft sneakers or ankle boots.
                  6)Bag – Denim or soft grey tote.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Jewellery – High ponytail; neon hoops & bangles.
                  2)Top – Fitted neon crop top or tank.
                  3)Bottom – Black wide-leg pants with neon accents or flared skirt.
                  4)Waist – Neon belt or chain detail.
                  5)Shoes – Chunky sneakers or platform sandals in neon.
                  6)Bag – Transparent neon mini backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek bun; gold hoops or bold studs.
                  2)Top – Structured wrap blouse in fiery red/mustard.
                  3)Bottom – High-waist pencil skirt or fitted trousers in dark tones.
                  4)Waist – Statement belt with metallic buckle.
                  5)Shoes – Sharp pointed heels or combat boots.
                  6)Bag – Structured handbag in red/mustard.''')

        elif shape==4:  
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Wavy hair for softness; colourful hoops.
                  2)Top – Bright peplum blouse in yellow or coral to create curves.
                  3)Bottom – Flared pants or A-line skirt in pastel.
                  4)Waist – Slim belt to fake definition.
                  5)Shoes – Strappy sandals in cheerful tones.
                  6)Bag – Fun crossbody in aqua or pink.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek braids; black choker.
                  2)Top – Fitted dark button-up shirt.
                  3)Bottom – Pleated skirt or straight pants in black.
                  4)Waist – Black belt with silver buckle.
                  5)Shoes – Chunky Mary Janes or platform boots.
                  6)Bag – Mini gothic satchel.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Low ponytail; tiny studs.
                  2)Top – Muted oversized knit in sage or dusty grey.
                  3)Bottom – Straight trousers in muted navy or taupe.
                  4)Waist – Skip belt, keep it flowy.
                  5)Shoes – Neutral loafers or sneakers.
                  6)Bag – Slouchy muted tote.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Glossy curls; sparkly earrings.
                  2)Top – Fitted crop top in hot pink or lavender.
                  3)Bottom – High-waist pastel mini skirt.
                  4)Waist – Glitter belt to create shape.
                  5)Shoes – Platform heels in bubblegum pink.
                  6)Bag – Barbie-style clutch.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose waves; pearl necklace.
                  2)Top – Vintage puff-sleeve blouse in cream or mustard.
                  3)Bottom – High-waist wide-leg trousers or midi skirt.
                  4)Waist – Brown vintage belt for shape.
                  5)Shoes – Retro block heels or Mary Janes.
                  6)Bag – Vintage satchel or crossbody.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Messy bun; delicate silver studs.
                  2)Top – Oversized cardigan in dusty navy.
                  3)Bottom – Straight-leg jeans in medium blue.
                  4)Waist – Keep unbelted, relaxed.
                  5)Shoes – Soft sneakers or ankle boots in grey.
                  6)Bag – Denim or faded blue tote.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Jewellery – High ponytail; neon earrings or bangles.
                  2)Top – Neon cropped hoodie or top (green/pink/orange).
                  3)Bottom – Black cargo pants with neon accents.
                  4)Waist – Neon chain belt.
                  5)Shoes – Chunky neon sneakers.
                  6)Bag – Transparent neon mini backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek bun; bold gold hoops.
                  2)Top – Structured fiery red or mustard jacket.
                  3)Bottom – Black straight trousers or leather skirt.
                  4)Waist – Gold-accented belt to fake curves.
                  5)Shoes – Combat boots or sharp heels in red/black.
                  6)Bag – Structured red or mustard handbag.''')
        elif shape==5: 
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Soft waves; colourful studs.
                  2)Top – Simple fitted tee in pastel yellow/pink (avoid extra volume on shoulders).
                  3)Bottom – Bright flared skirt or wide-leg pants to balance.
                  4)Waist – Cute slim belt in cheerful tone.
                  5)Shoes – Strappy wedges or block heels.
                  6)Bag – Fun colourful tote.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Braids; silver cross necklace.
                  2)Top – Fitted black blouse with plain neckline (avoid puffed shoulders).
                  3)Bottom – A-line skirt or pleated mini in dark plaid/black.
                  4)Waist – Thin belt for subtle balance.
                  5)Shoes – Chunky Mary Janes or lace-up boots.
                  6)Bag – Black structured mini satchel.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Low bun; tiny studs.
                  2)Top – Slim muted knit in sage or dusty grey.
                  3)Bottom – Wide-leg trousers or midi skirt in muted navy/taupe to add volume.
                  4)Waist – Skip belt for relaxed vibe.
                  5)Shoes – Neutral loafers or sneakers.
                  6)Bag – Slouchy muted tote.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Glossy hairband; sparkly earrings.
                  2)Top – Fitted corset or crop top in pink/purple (simple neckline).
                  3)Bottom – Pastel flared mini skirt or wide-leg trousers to balance.
                  4)Waist – Glitter slim belt.
                  5)Shoes – Platform heels in Barbie pink.
                  6)Bag – Barbie-style mini clutch.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Soft curls; pearl necklace.
                  2)Top – Simple blouse (avoid shoulder details) in cream or dusty rose.
                  3)Bottom – Wide-leg trousers or flowy skirt in earthy vintage shades.
                  4)Waist – Vintage belt in brown/tan.
                  5)Shoes – Retro loafers or Mary Janes.
                  6)Bag – Mini vintage satchel.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Messy bun; delicate silver studs.
                  2)Top – Plain fitted cardigan or blouse in dusty navy.
                  3)Bottom – Straight jeans or palazzo pants in blue to balance.
                  4)Waist – Leave unbelted, natural shape.
                  5)Shoes – Soft sneakers or ankle boots in grey/blue.
                  6)Bag – Denim or faded blue tote.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Ponytail; neon earrings.
                  2)Top – Simple neon tank/tee (avoid shoulder padding).
                  3)Bottom – Black cargo pants or skirt with neon accents.
                  4)Waist – Neon chain belt.
                  5)Shoes – Chunky neon sneakers.
                  6)Bag – Transparent neon mini backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek bun; bold hoops.
                  2)Top – Structured fitted blouse in fiery red/mustard (avoid puff sleeves).
                  3)Bottom – Dark A-line skirt or wide trousers to balance.
                  4)Waist – Gold-accented belt.
                  5)Shoes – Combat boots or sharp pointed heels.
                  6)Bag – Structured red/mustard handbag.''')
        elif shape==6:
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Half-up hair with bright clips; colourful dangly earrings.
                  2)Top – V-neck blouse or wrap top in sunshine yellow/coral to highlight neckline.
                  3)Bottom – Straight trousers or flowy A-line skirt in white/pastel.
                  4)Waist – Belt slightly higher (empire line) in a fun bright shade.
                  5)Shoes – Strappy wedges or colourful block heels.
                  6)Bag – Mini crossbody in bright pop colours.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek straight hair; layered chokers and silver rings.
                  2)Top – Flowy black blouse with lace or mesh sleeves, V-neck to elongate.
                  3)Bottom – High-rise dark trousers or midi skirt for balance.
                  4)Waist – Wide gothic belt placed higher to create structure.
                  5)Shoes – Chunky black boots or platform Mary Janes.
                  6)Bag – Black structured satchel with silver details.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Low bun; soft delicate studs.
                  2)Top – Loose soft blouse or oversized knit in sage, dusty rose, or grey.
                  3)Bottom – Straight or slightly flared trousers in muted navy or taupe.
                  4)Waist – Tie belt at empire line for comfort and shape.
                  5)Shoes – Simple flats, loafers, or soft sneakers.
                  6)Bag – Slouchy tote in muted earthy tones.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Glossy curls; sparkly hoops and layered gold chains.
                  2)Top – Off-shoulder or wrap crop top in Barbie pink/lavender (draws attention upward).
                  3)Bottom – Straight or A-line mini skirt in pastel or white.
                  4)Waist – Glitter belt or pearl-detailed slim belt just under bust.
                  5)Shoes – Strappy platform heels in pink/silver/white.
                  6)Bag – Mini glitter clutch or holographic handbag.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Soft waves; pearl earrings and vintage pendant.
                  2)Top – Puff-sleeve blouse or peter-pan collar shirt in cream/dusty rose.
                  3)Bottom – Straight culottes or midi skirt in earthy olive, brown, or burgundy.
                  4)Waist – Wide belt above natural waist for definition.
                  5)Shoes – Vintage loafers or low block-heeled boots.
                  6)Bag – Small structured satchel in tan/green tones.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose ponytail or low bun; minimal silver studs.
                  2)Top – Relaxed V-neck knit or blouse in light blue/slate grey.
                  3)Bottom – Straight trousers or flowy palazzos in deep navy.
                  4)Waist – Soft slim belt (optional) for shape.
                  5)Shoes – Comfortable flats or ankle boots in grey/blue/white.
                  6)Bag – Soft crossbody or tote in denim blue.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Jewellery – High ponytail; neon chunky hoops; acrylic bangles.
                  2)Top – Neon wrap blouse or cropped hoodie in green/pink/orange.
                  3)Bottom – Black straight trousers or skirt with neon stripe details.
                  4)Waist – Neon belt slightly above natural waist.
                  5)Shoes – Chunky neon sneakers or platform sandals.
                  6)Bag – Transparent neon mini backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek high ponytail; bold gold hoops.
                  2)Top – Structured wrap blouse or cropped jacket in fiery red/mustard.
                  3)Bottom – Black trousers or straight skirt to slim the lower half.
                  4)Waist – Wide metallic belt placed high to define waist.
                  5)Shoes – Sharp heels or combat boots in red/black.
                  6)Bag – Structured handbag in red with metallic accents.''')
        elif shape==7:  
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Loose waves; colourful studs or playful hoops.
                  2)Top – Relaxed V-neck blouse in sunshine yellow or coral to soften shoulders.
                  3)Bottom – High-waist A-line skirt or wide trousers in pastel/white (adds volume below).
                  4)Waist – Fun slim belt in neon or metallic shade.
                  5)Shoes – Bright block heels or colourful sandals.
                  6)Bag – Mini crossbody in bold pop colour.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Sleek straight hair; black choker, silver rings.
                  2)Top – Fitted black blouse with lace/mesh, deep neckline to break shoulder line.
                  3)Bottom – A-line skirt or pleated mini in plaid/black to balance shape.
                  4)Waist – Slim dark belt with silver buckle.
                  5)Shoes – Chunky boots or Mary Janes.
                  6)Bag – Structured satchel with gothic metallic accents.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Low ponytail; minimal studs.
                  2)Top – Loose blouse or knit in sage, dusty rose, or soft grey.
                  3)Bottom – Wide-leg trousers or flowy skirt in muted navy or taupe to soften lines.
                  4)Waist – Neutral thin belt, or leave unbelted.
                  5)Shoes – Simple flats, loafers, or sneakers in muted tones.
                  6)Bag – Slouchy tote in earthy beige or soft clay.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Glossy curls; sparkly hoops or butterfly clips.
                  2)Top – Sweetheart neckline or wrap crop top in Barbie pink/lavender (softens shoulder width).
                  3)Bottom – Flared skirt or wide-leg trousers in pastel shades to balance.
                  4)Waist – Glitter belt or pearl belt to cinch softly.
                  5)Shoes – Strappy heels, cute sneakers, or glitter sandals.
                  6)Bag – Mini shoulder bag or sparkly clutch.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Soft waves; pearl studs or vintage brooch.
                  2)Top – Peter-pan collar blouse or puff-sleeve shirt in cream, dusty rose, or muted mustard.
                  3)Bottom – High-waist culottes or midi skirt with flow to add volume at hips.
                  4)Waist – Woven or leather belt at natural waist.
                  5)Shoes – Vintage-inspired loafers or low block boots.
                  6)Bag – Structured satchel in tan, deep green, or burgundy.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Low bun; simple silver studs.
                  2)Top – Relaxed V-neck blouse or oversized knit in light/dusty blue.
                  3)Bottom – Straight trousers or flowy skirt in deeper navy or denim.
                  4)Waist – Soft belt in muted navy.
                  5)Shoes – Comfortable flats, sneakers, or ankle boots.
                  6)Bag – Soft tote or crossbody in denim blue or slate grey.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Jewellery – High ponytail; neon hoops; chunky bangles.
                  2)Top – Neon wrap crop or mesh top in pink/green/orange to stand out.
                  3)Bottom – High-waist flared trousers or skirt in black with neon accents.
                  4)Waist – Neon chain belt for edge.
                  5)Shoes – Chunky sneakers or platform sandals in neon mixes.
                  6)Bag – Transparent holographic backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Jewellery – Slick ponytail or bun; bold gold hoops.
                  2)Top – Structured V-neck blouse or cropped jacket in fiery red or mustard (draws vertical lines).
                  3)Bottom – High-waist straight trousers or skirt in black/oxblood to ground the look.
                  4)Waist – Bold metallic belt for power.
                  5)Shoes – Sharp heels or block boots in red/black/gold.
                  6)Bag – Structured crossbody or handbag with metallic accents.''')
    elif gender=='M':
        if shape==1:   
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean fade or short hairstyle; sporty watch, minimal necklace.
                  2)Top – Bright polo shirt or crew-neck tee in yellow, aqua, or coral to broaden shoulders.
                  3)Bottom – Slim-fit chinos or straight trousers in beige/white to slim hips.
                  4)Layer – Lightweight blazer or denim jacket to add structure to shoulders.
                  5)Shoes – White sneakers or loafers for a lively vibe.
                  6)Bag – Casual backpack or messenger in a fun bright tone.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slicked-back or middle-part hair; leather bracelet, black watch.
                  2)Top – Fitted black button-up or dark graphic tee to draw attention upward.
                  3)Bottom – Slim black jeans or tailored trousers to elongate legs.
                  4)Layer – Longline coat or bomber in charcoal/black for structure.
                  5)Shoes – Combat boots, dark sneakers, or Chelsea boots.
                  6)Bag – Black crossbody or leather satchel with silver accents.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Accessories – Soft casual hairstyle; muted strap watch.
                  2)Top – Relaxed henley or knit in muted grey, sage, or taupe to soften vibe.
                  3)Bottom – Straight trousers or jeans in navy/charcoal (not skinny).
                  4)Layer – Overshirt or muted jacket to balance proportions.
                  5)Shoes – Neutral sneakers or suede loafers in muted beige/grey.
                  6)Bag – Slouchy backpack or muted-toned messenger.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean hairstyle; gold chain or trendy ring; stylish watch.
                  2)Top – Pastel button-up (pink, lavender, sky blue) or fitted tee.
                  3)Bottom – White chinos or tailored pastel trousers to lengthen legs.
                  4)Layer – Cropped jacket or fitted blazer for trendy vibes.
                  5)Shoes – White sneakers or pastel-toned loafers.
                  6)Bag – Mini sling bag or trendy crossbody in pastel shades.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Accessories – Soft side part; vintage-inspired watch; round glasses.
                  2)Top – Earth-tone shirt (olive, burgundy, cream) tucked in.
                  3)Bottom – High-waist trousers with pleats in brown or navy.
                  4)Layer – Vintage blazer, corduroy, or cardigan.
                  5)Shoes – Classic loafers, brogues, or boots.
                  6)Bag – Leather satchel or vintage crossbody.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Accessories – Low-maintenance hairstyle; silver/blue strap watch.
                  2)Top – Cozy knit or relaxed shirt in navy, dusty blue, or teal.
                  3)Bottom – Straight jeans or trousers in darker blue.
                  4)Layer – Denim jacket or bomber in navy tones.
                  5)Shoes – Blue-toned sneakers, grey loafers, or white slip-ons.
                  6)Bag – Denim or grey casual backpack.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Accessories – Spiked or styled hair; bold neon watch; funky bracelet.
                  2)Top – Neon graphic tee or hoodie in pink, green, or orange.
                  3)Bottom – Black jeans with neon stripes or slim joggers.
                  4)Layer – Neon windbreaker or bomber jacket.
                  5)Shoes – Chunky sneakers in neon mixes.
                  6)Bag – Neon crossbody or transparent backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Accessories – Sharp hairstyle; bold red strap watch; metallic ring.
                  2)Top – Fitted red or mustard shirt with structured shoulders.
                  3)Bottom – Black slim trousers or dark jeans to slim hips.
                  4)Layer – Leather jacket or sharp blazer for dominance.
                  5)Shoes – Combat boots, leather loafers, or sneakers in red/black.
                  6)Bag – Structured red or dark leather backpack.''')
        elif shape==2:   
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean short haircut; sporty digital watch.
                  2)Top – Bright V-neck or open-collar shirt in yellow, aqua, or coral (draws eyes upward).
                  3)Bottom – Straight trousers or dark slim chinos to balance midsection.
                  4)Layer – Lightweight open jacket or blazer to add vertical lines.
                  5)Shoes – White trainers, slip-on loafers, or colourful sneakers.
                  6)Bag – Messenger or backpack in a fun, bright colour.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slicked hair or fade; leather strap watch.
                  2)Top – Black button-up or fitted tee with vertical detail (elongates torso).
                  3)Bottom – Dark slim trousers or jeans to create lean lines.
                  4)Layer – Longline cardigan, trench, or leather jacket for structure.
                  5)Shoes – Black Chelsea boots or dark trainers.
                  6)Bag – Black crossbody or slim satchel.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Accessories – Soft casual hairstyle; muted watch.
                  2)Top – Relaxed henley or knit polo in soft grey, olive, or taupe.
                  3)Bottom – Straight trousers in navy or muted brown.
                  4)Layer – Casual overshirt or muted cardigan to soften torso.
                  5)Shoes – Neutral loafers, trainers, or desert boots.
                  6)Bag – Slouchy muted backpack or messenger.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean hairstyle; gold chain or stylish bracelet.
                  2)Top – Pastel shirt (lavender, pink, sky blue) or trendy fitted tee with V-neck.
                  3)Bottom – Slim white chinos or pastel trousers to elongate.
                  4)Layer – Cropped pastel jacket or blazer.
                  5)Shoes – White sneakers or loafers in pastel tones.
                  6)Bag – Trendy crossbody in pastel or metallic finish.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Accessories – Soft side part; vintage glasses; leather strap watch.
                  2)Top – Earthy shirt in cream, burgundy, or mustard (keeps focus upward).
                  3)Bottom – Straight trousers in tan, olive, or navy.
                  4)Layer – Vintage-inspired blazer, cardigan, or trench.
                  5)Shoes – Loafers, oxfords, or suede boots.
                  6)Bag – Leather satchel or vintage messenger.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed hairstyle; simple blue strap watch.
                  2)Top – Loose sweater or relaxed tee in dusty navy or teal.
                  3)Bottom – Straight navy trousers or mid-wash jeans.
                  4)Layer – Casual bomber or denim jacket.
                  5)Shoes – Grey trainers or navy loafers.
                  6)Bag – Casual denim or blue-toned backpack.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Accessories – Fun spiked hair or styled look; bold neon watch.
                  2)Top – Neon hoodie or tee in pink, green, or orange with graphics.
                  3)Bottom – Black slim joggers or neon-detailed trousers.
                  4)Layer – Neon bomber or windbreaker.
                  5)Shoes – Chunky neon sneakers or high-tops.
                  6)Bag – Transparent neon backpack or crossbody.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Accessories – Sharp hairstyle; bold metallic watch.
                  2)Top – Structured red or mustard shirt with sharp collar.
                  3)Bottom – Slim dark jeans or tailored trousers.
                  4)Layer – Black leather jacket or fitted blazer for strong lines.
                  5)Shoes – Combat boots or pointed dress shoes in black/red.
                  6)Bag – Structured leather satchel in dark red or black.''')
        elif shape==3:   
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Accessories – Neat side part or fade; fun colourful watch.
                  2)Top – Bright fitted polo or open-collar shirt in yellow, aqua, or coral (keeps attention upward).
                  3)Bottom – Slim trousers or chinos in beige, grey, or white (balances shape).
                  4)Layer – Lightweight bomber or casual blazer.
                  5)Shoes – White sneakers or casual loafers.
                  6)Bag – Crossbody or backpack in a cheerful bright tone.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slick hair or undercut; black strap watch.
                  2)Top – Black fitted shirt, turtleneck, or collared tee.
                  3)Bottom – Slim black trousers or jeans to elongate.
                  4)Layer – Longline coat or leather jacket for sleek lines.
                  5)Shoes – Black boots, derbies, or lace-ups.
                  6)Bag – Structured black satchel or slim messenger.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed hairstyle; neutral strap watch.
                  2)Top – Soft knit polo, henley, or crewneck in muted grey, sage, or navy.
                  3)Bottom – Slim trousers in navy, taupe, or muted brown.
                  4)Layer – Soft cardigan or casual overshirt.
                  5)Shoes – Neutral sneakers, loafers, or slip-ons.
                  6)Bag – Slouchy muted messenger or casual tote.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Accessories – Fresh hairstyle; sleek chain necklace or minimal bracelet.
                  2)Top – Pastel fitted shirt or trendy tee (pink, lavender, sky blue).
                  3)Bottom – White chinos or slim trousers in blush/beige.
                  4)Layer – Light pastel jacket or cropped blazer.
                  5)Shoes – White trainers, pastel loafers, or clean sneakers.
                  6)Bag – Mini trendy crossbody or pastel-toned satchel.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Accessories – Side part or soft waves; round vintage glasses; brown leather strap watch.
                  2)Top – Earthy-toned shirt in cream, burgundy, or mustard.
                  3)Bottom – Slim trousers or chinos in olive, navy, or deep tan.
                  4)Layer – Vintage cardigan, corduroy jacket, or structured blazer.
                  5)Shoes – Brown brogues, loafers, or suede boots.
                  6)Bag – Leather satchel, messenger, or structured vintage backpack.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed natural hairstyle; simple navy strap watch.
                  2)Top – Loose-fit sweater, henley, or polo in dusty navy or muted teal.
                  3)Bottom – Slim straight trousers or dark jeans in navy/grey.
                  4)Layer – Casual bomber, denim jacket, or hoodie.
                  5)Shoes – Grey trainers, loafers, or neutral sneakers.
                  6)Bag – Casual blue-toned tote or denim backpack.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Accessories – Fun spiked or edgy hairstyle; neon strap watch.
                  2)Top – Neon printed hoodie, graphic tee, or cropped bomber.
                  3)Bottom – Slim joggers or fitted trousers with neon details.
                  4)Layer – Neon windbreaker or varsity jacket.
                  5)Shoes – Chunky neon sneakers or statement high-tops.
                  6)Bag – Transparent or neon backpack/crossbody.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Accessories – Sharp haircut; metallic strap watch or bold cuff.
                  2)Top – Structured fiery red, maroon, or mustard shirt.
                  3)Bottom – Slim black or dark grey trousers to add edge.
                  4)Layer – Black leather jacket or tailored blazer.
                  5)Shoes – Combat boots, block dress shoes, or pointed loafers.
                  6)Bag – Structured leather satchel or messenger in deep red/black.''')
        elif shape==4:   
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Accessories – Fresh fade or quiff; colourful strap watch.
                  2)Top – Bright polo, crewneck, or casual shirt in yellow, aqua, or pink.
                  3)Bottom – Slim chinos or tapered trousers in beige, cream, or light grey.
                  4)Layer – Lightweight bomber or bright jacket to add dimension.
                  5)Shoes – White sneakers, espadrilles, or casual loafers.
                  6)Bag – Cheerful crossbody or backpack in bold tones.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slick side part or undercut; black metal strap watch.
                  2)Top – Black fitted shirt, slim turtleneck, or dark patterned button-up.
                  3)Bottom – Slim black trousers or skinny jeans to sharpen shape.
                  4)Layer – Leather jacket or structured long coat.
                  5)Shoes – Black lace-up boots, Chelsea boots, or derbies.
                  6)Bag – Structured black briefcase or satchel with silver details.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed hair; muted strap watch.
                  2)Top – Soft knit henley, casual button-up, or polo in muted tones (sage, grey, navy).
                  3)Bottom – Slim trousers or chinos in muted beige, taupe, or navy.
                  4)Layer – Soft cardigan, overshirt, or casual bomber.
                  5)Shoes – Neutral sneakers, loafers, or simple slip-ons.
                  6)Bag – Relaxed tote or muted messenger bag.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean hairstyle; minimal bracelet or light chain.
                  2)Top – Pastel shirt or fitted tee (lavender, pink, or sky blue).
                  3)Bottom – White or beige slim trousers to keep it soft.
                  4)Layer – Light jacket or pastel cardigan.
                  5)Shoes – White trainers or pastel loafers.
                  6)Bag – Trendy pastel crossbody or mini satchel.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Accessories – Neatly styled hair; vintage-style glasses; leather strap watch.
                  2)Top – Earthy toned shirt (cream, burgundy, muted mustard).
                  3)Bottom – Slim trousers or chinos in olive, navy, or deep brown.
                  4)Layer – Vintage-inspired cardigan, tweed blazer, or corduroy jacket.
                  5)Shoes – Brown loafers, brogues, or suede boots.
                  6)Bag – Leather messenger or vintage satchel.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Accessories – Simple relaxed hair; navy strap watch.
                  2)Top – Cozy knit sweater, henley, or polo in dusty blue or slate teal.
                  3)Bottom – Slim trousers or dark jeans in navy, charcoal, or muted grey.
                  4)Layer – Casual denim jacket or soft bomber.
                  5)Shoes – Blue toned sneakers, loafers, or slip-ons.
                  6)Bag – Denim or navy casual backpack.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Accessories – Spiky/edgy hair; neon strap watch or fun bracelet.
                  2)Top – Neon hoodie, graphic tee, or cropped bomber.
                  3)Bottom – Slim joggers or fitted trousers with neon detailing.
                  4)Layer – Neon varsity jacket or zip-up windbreaker.
                  5)Shoes – Neon sneakers or bold chunky trainers.
                  6)Bag – Neon or transparent crossbody/backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Accessories – Sharp haircut; bold cuff bracelet or metallic watch.
                  2)Top – Strong fiery red, maroon, or mustard shirt.
                  3)Bottom – Slim black or dark trousers to add intensity.
                  4)Layer – Black leather jacket or sharp tailored blazer.
                  5)Shoes – Combat boots or strong pointed loafers.
                  6)Bag – Structured satchel or messenger in deep red/black.''')
        elif shape==5:   
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Accessories – Fresh undercut or quiff; colourful bracelet or bright watch.
                  2)Top – Slim-fit polo or tee in sunshine yellow, aqua, or coral (keeps attention balanced on wide shoulders).
                  3)Bottom – Straight or slightly relaxed trousers/chinos in beige or cream.
                  4)Layer – Lightweight bomber or denim jacket in a soft tone.
                  5)Shoes – White trainers, loafers, or espadrilles.
                  6)Bag – Crossbody in a bright pop colour.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slick hairstyle; silver ring or chain; black leather watch.
                  2)Top – Fitted dark button-up or turtleneck (black, charcoal, or deep burgundy).
                  3)Bottom – Slim or straight trousers in black/dark plaid to soften shoulder dominance.
                  4)Layer – Longline coat or leather jacket to elongate frame.
                  5)Shoes – Chelsea boots, lace-up derbies, or black sneakers.
                  6)Bag – Structured black satchel or leather backpack.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed hairstyle; muted strap watch.
                  2)Top – Casual henley, knit, or loose shirt in muted sage, soft grey, or dusty navy.
                  3)Bottom – Straight chinos or drawstring trousers in beige, taupe, or muted blue.
                  4)Layer – Soft cardigan or unstructured jacket to balance shoulders.
                  5)Shoes – Neutral sneakers or loafers in grey, brown, or navy.
                  6)Bag – Soft tote or slouchy messenger bag.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean hairstyle; dainty chain or soft bracelet.
                  2)Top – Pastel tee or fitted polo (lavender, pink, sky blue).
                  3)Bottom – White or beige trousers to soften wide upper body.
                  4)Layer – Pastel jacket or light bomber.
                  5)Shoes – White trainers or soft pastel loafers.
                  6)Bag – Trendy mini satchel or pastel crossbody.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slick hairstyle; vintage watch or retro glasses.
                  2)Top – Neutral toned shirt (cream, olive, muted burgundy).
                  3)Bottom – Relaxed chinos or pleated trousers to balance shoulders.
                  4)Layer – Tweed blazer, corduroy overshirt, or wool cardigan.
                  5)Shoes – Brown leather brogues, loafers, or suede boots.
                  6)Bag – Classic leather satchel or vintage messenger bag.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed natural hairstyle; navy strap watch.
                  2)Top – Cozy knit pullover, polo, or casual shirt in dusty blue or slate teal.
                  3)Bottom – Dark straight jeans or slim trousers to elongate silhouette.
                  4)Layer – Casual denim jacket or bomber in navy.
                  5)Shoes – Muted sneakers or slip-ons in blue/grey.
                  6)Bag – Denim or navy backpack.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Accessories – Spiky or edgy hairstyle; neon watch or cuff.
                  2)Top – Neon tee, cropped hoodie, or graphic bomber (pink, green, or orange).
                  3)Bottom – Black joggers or slim trousers with neon detailing.
                  4)Layer – Neon varsity jacket or windbreaker.
                  5)Shoes – Neon sneakers or chunky trainers.
                  6)Bag – Transparent or neon backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Accessories – Sharp cut; bold metallic bracelet or strong watch.
                  2)Top – Structured fiery red, maroon, or mustard shirt/jacket.
                  3)Bottom – Slim black trousers or jeans to ground broad shoulders.
                  4)Layer – Sharp leather jacket or tailored blazer.
                  5)Shoes – Combat boots, pointed loafers, or bold derbies.
                  6)Bag – Structured messenger or satchel in deep red/black.''')
        elif shape==6:  
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Accessories – Short clean haircut or side part; colourful watch or simple bracelet.
                  2)Top – V-neck or open-collar shirt in bright cheerful colours (yellow, aqua, coral) to elongate neck and brighten mood.
                  3)Bottom – Straight dark trousers or jeans to balance midsection.
                  4)Layer – Lightweight open jacket or casual blazer in pastel.
                  5)Shoes – Bright sneakers or loafers in white/colour pop.
                  6)Bag – Crossbody in a playful shade.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slicked back hair; silver chain or leather bracelet.
                  2)Top – Dark button-up or polo in black, deep navy, or burgundy (slimming effect).
                  3)Bottom – Straight or slim trousers in charcoal/black.
                  4)Layer – Longline coat or dark bomber jacket to streamline silhouette.
                  5)Shoes – Chelsea boots or dark sneakers.
                  6)Bag – Structured leather satchel in black.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed hairstyle; muted leather strap watch.
                  2)Top – Open relaxed shirt or knit in muted tones (sage, taupe, soft grey).
                  3)Bottom – Straight chinos or joggers in earthy tones to balance proportions.
                  4)Layer – Soft cardigan or casual unstructured jacket.
                  5)Shoes – Comfortable loafers or sneakers in neutral shades.
                  6)Bag – Slouchy messenger or canvas tote.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean hairstyle; pastel bracelet or light chain.
                  2)Top – Pastel shirt, polo, or casual tee (lavender, blush, sky blue).
                  3)Bottom – Slim dark trousers to ground look.
                  4)Layer – Pastel bomber or denim jacket to add softness.
                  5)Shoes – White sneakers or pastel loafers.
                  6)Bag – Trendy pastel crossbody.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slick hair or side-part; retro glasses, vintage watch.
                  2)Top – Neutral shirt (cream, olive, muted burgundy) with vertical details to elongate torso.
                  3)Bottom – Straight trousers or chinos in earthy tones.
                  4)Layer – Vintage-inspired blazer or corduroy jacket.
                  5)Shoes – Brown brogues, loafers, or suede boots.
                  6)Bag – Leather satchel or vintage backpack.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed hairstyle; navy strap watch.
                  2)Top – Comfortable knit or casual shirt in dusty blue, slate, or teal to soften silhouette.
                  3)Bottom – Straight jeans or trousers in darker tones for length.
                  4)Layer – Denim jacket, bomber, or casual zip-up in navy.
                  5)Shoes – Neutral sneakers or slip-ons in blue/grey.
                  6)Bag – Denim or navy backpack.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Accessories – Edgy hairstyle; neon cuff or digital watch.
                  2)Top – Neon graphic tee or cropped hoodie layered with open shirt/jacket.
                  3)Bottom – Slim joggers or trousers with neon stripes to elongate legs.
                  4)Layer – Bright bomber or varsity jacket.
                  5)Shoes – Neon trainers or chunky sneakers.
                  6)Bag – Transparent or neon backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Accessories – Sharp haircut; bold watch or metallic bracelet.
                  2)Top – Structured shirt or jacket in fiery red, maroon, or mustard-yellow.
                  3)Bottom – Dark trousers or jeans with clean straight cut.
                  4)Layer – Bold leather jacket or sharp blazer.
                  5)Shoes – Combat boots or bold loafers in black/red.
                  6)Bag – Structured leather messenger in deep red/black.''')
        elif shape==7:  
            if mood==1:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean haircut or fade; playful bracelet or colourful watch.
                  2)Top – Polo shirt or casual tee in cheerful colours (yellow, aqua, coral) – trapezoid shape allows bold colours.
                  3)Bottom – Slim chinos or fitted jeans in light beige, white, or denim.
                  4)Layer – Lightweight bomber or casual blazer in pastel.
                  5)Shoes – White sneakers or loafers with a pop of colour.
                  6)Bag – Crossbody bag in fun tones.''')
            elif mood==2:
                print('''You can design yourself as:
                  1)Hair & Accessories – Slick hairstyle; black leather bracelet or silver chain.
                  2)Top – Fitted button-up shirt in black, burgundy, or navy (shows off balanced frame).
                  3)Bottom – Slim dark trousers or tailored jeans.
                  4)Layer – Leather jacket or dark bomber.
                  5)Shoes – Lace-up boots or sleek loafers in black.
                  6)Bag – Structured messenger in black leather.''')
            elif mood==3:
                print('''You can design yourself as:
                  1)Hair & Accessories – Soft hairstyle; muted strap watch.
                  2)Top – Relaxed linen shirt or knit in earthy/muted tones (sage, beige, soft grey).
                  3)Bottom – Straight chinos in taupe, navy, or olive.
                  4)Layer – Cardigan or unstructured jacket for balance.
                  5)Shoes – Loafers, slip-ons, or relaxed sneakers in neutral.
                  6)Bag – Soft tote or messenger in muted shades.''')
            elif mood==4:
                print('''You can design yourself as:
                  1)Hair & Accessories – Clean fade or side part; trendy necklace or pastel bracelet.
                  2)Top – Pastel shirt, tee, or polo (lavender, blush, sky blue).
                  3)Bottom – Slim white trousers or light denim.
                  4)Layer – Casual pastel jacket or overshirt.
                  5)Shoes – White or pastel sneakers.
                  6)Bag – Mini crossbody in pastel shade.''')
            elif mood==5:
                print('''You can design yourself as:
                  1)Hair & Accessories – Vintage glasses, classic watch.
                  2)Top – Fitted shirt in earthy retro tones (mustard, burgundy, olive).
                  3)Bottom – Slim chinos or trousers in deep brown, navy, or khaki.
                  4)Layer – Corduroy jacket, blazer, or retro bomber.
                  5)Shoes – Leather brogues, loafers, or boots in brown/oxblood.
                  6)Bag – Structured satchel or retro-inspired backpack.''')
            elif mood==6:
                print('''You can design yourself as:
                  1)Hair & Accessories – Relaxed hairstyle; navy strap watch or simple bracelet.
                  2)Top – Cozy knit, henley, or tee in dusty blue, teal, or slate.
                  3)Bottom – Straight jeans or chinos in navy or darker blue.
                  4)Layer – Denim jacket, casual bomber, or hoodie in blue tones.
                  5)Shoes – Neutral sneakers or slip-ons in grey/navy.
                  6)Bag – Casual backpack in blue or grey.''')
            elif mood==7:
                print('''You can design yourself as:
                  1)Hair & Accessories – Trendy hairstyle; neon bracelet or bold cap.
                  2)Top – Neon graphic tee or cropped hoodie layered with open overshirt.
                  3)Bottom – Slim joggers, fitted jeans, or trousers with neon detailing.
                  4)Layer – Neon-accent bomber or varsity jacket.
                  5)Shoes – Chunky neon sneakers or colourful high-tops.
                  6)Bag – Neon crossbody or transparent backpack.''')
            elif mood==8:
                print('''You can design yourself as:
                  1)Hair & Accessories – Sharp haircut; metallic bracelet or bold watch.
                  2)Top – Structured shirt, polo, or fitted jacket in fiery red, maroon, or mustard-yellow.
                  3)Bottom – Slim dark jeans or tailored trousers.
                  4)Layer – Leather biker jacket or sharp blazer.
                  5)Shoes – Combat boots, block loafers, or high-top sneakers in black/red.
                  6)Bag – Bold leather messenger in deep red or black.''')
    again = input("\nDo you want to try again? (Yes/No): ")
    if again=="No":
        print("Thanks for styling with us 💖 Goodbye!")
        break








