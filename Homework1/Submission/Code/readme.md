Problem 1: Classify an image as either an advertisement or not an advertisement given information on the geometry of the image, phrases in the image, and url tags.

Feature Information:

Number of Attributes: 1558 (3 continuous; others binary)
height: continuous.
width: continuous.
aratio: continuous.
local: 0,1.
| 457 features from url terms, each of the form "url*term1+term2...";
| for example:
url*images+buttons: 0,1.
  ...
| 495 features from origurl terms, in same form; for example:
origurl*labyrinth: 0,1.
  ...
| 472 features from ancurl terms, in same form; for example:
ancurl*search+direct: 0,1.
  ...
| 111 features from alt terms, in same form; for example:
alt*your: 0,1.
  ...
| 19 features from caption terms
caption*and: 0,1.

==========================================================================================================================

Problem 2: Predict which of five heuristics will prove a theorem quickest when used by a first-order prover. The sixth heuristic is to refuse attempting the proof if the theorem is predicted too difficult.

Feature Information:

Columns 1 to 14 are the static features and columns 15 to 53 are the dynamic features. The final five columns denote the time in seconds taken by each of the five heuristics to prove the relevant theorem. There was a time limit of 100 seconds.  An entry of -100 denotes failure to obtain a proof within the time limit.

===========================================================================================================================

Problem 3: Predict whether or not someone makes over $50,000/year from consensus data.

Feature Information:

age: continuous.
workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
fnlwgt: continuous.
education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
education-num: continuous.
marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
sex: Female, Male.
capital-gain: continuous.
capital-loss: continuous.
hours-per-week: continuous.
native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.
