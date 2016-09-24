#READ ME - Where is the South?
##Summary
I am from North Carolina originally, but attended college in upstate New York, and currently work in New York City. 
Therefore, this article on fivethirtyeight: http://fivethirtyeight.com/datalab/which-states-are-in-the-south/ especially resonated with me, as it is a conversation I have often had (in jest) with friends.
There is more debate about which states are actually in the south than one would think.


##Design:
The goal is to show consensus about which states are truly in the south. 
This is most effectively done using a map, where the color scale is indicative of how many votes a given state got as "southern".
I used a divergent color scale from color brewer, as I believe it makes the differences in votes more apparent than a single color scale.
To bring this to the next level, investigating how various regions of the US percieve which states are really southern is a very interesting investigation.
This interaction is enabled with filter buttons on the left.
Tooltips enable the user to see specifically how many votes a given state got.
Legend shows how many votes each state got and what the color represents on the map.
"All" is set as the default filter, and is colored differently to distiguish from the others.
When a button is selected, its color is changed to be a darker blue.
Added a header to the filters to make it more clear what they are.
North Carolina is highlighted to make the central theme of my home state being southern more apparent.
I have included a short description at the top of the visualisation to provide some initial context for the reader.


##Feedback:
###Oliver 
- Perhaps add states votes on top of the state?
- Highlighting seems like you are deselecting the button not selecting it (make the selected button darker and the other ones lighter)
- Format all or none buttons differently
- The yellow color scale makes the white borders of the states hard to see
- Likes the opacity change when you hover

To account for Oliver's feedback I made the following changes:
- Added black borders to the states
- changed the color scheme of the filter buttons (default color is light blue, and selected color is darker blue)
- Put All at the top of the buttons and None at the bottom

###Oye
- Need a legend for the colors
- Name of state shown by default?
- Order the buttons alphabetically 
- Can you enable zoom/pan?

To account for Oye's feedback I made the following changes:
 - Created a legend for the color scale
 - Ordered the buttons alphabetically (except for All and None)
 - The rest of his feedback was not necessary for this viz

###Roshni:
- What do the colors mean?
- What do the filters mean?
- Diverging color scale may be a bit confusing (perhaps legend would fix this)

Adding a label to the filter buttons, and adding the legend attended to most of Roshni's questions.


##Resources:
Data Source - https://github.com/fivethirtyeight/data/tree/master/region-survey
https://github.com/d3/d3-3.x-api-reference/blob/master/CSV.md
http://bl.ocks.org/michellechandra/0b2ce4923dc9b5809922
https://github.com/alignedleft/d3-book/blob/master/chapter_12/05_choropleth.html
https://github.com/alignedleft/d3-book/tree/master/chapter_12
http://www.w3schools.com/cssref/pr_font_weight.asp
http://stackoverflow.com/questions/2647867/how-to-determine-if-variable-is-undefined-or-null
http://colorbrewer2.org/
http://d3-legend-v3.susielu.com/
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
http://stackoverflow.com/questions/25168086/sorting-objects-based-on-property-value-in-d3
http://bl.ocks.org/rgdonohue/9280446
https://bost.ocks.org/mike/join/