import operator
import turtle
wn=turtle.Screen()



def speech():
    AndrewJackson=["ABOUT to undertake the arduous duties that I have been appointed to perform by the choice of a free people, I avail myself of this customary and solemn occasion to express the gratitude which their confidence inspires and to acknowledge the accountability which my situation enjoins. While the magnitude of their interests convinces me that no thanks can be adequate to the honor they have conferred, it admonishes me that the best return I can make is the zealous dedication of my humble abilities to their service and their good. "
    "As the instrument of the Federal Constitution it will devolve on me for a stated period to execute the laws of the United States, to superintend their foreign and their confederate relations, to manage their revenue, to command their forces, and, by communications to the Legislature, to watch over and to promote their interests generally. And the principles of action by which I shall endeavor to accomplish this circle of duties it is now proper for me briefly to explain."
    "In administering the laws of Congress I shall keep steadily in view the limitations as well as the extent of the Executive power, trusting thereby to discharge the functions of my office without transcending its authority. With foreign nations it will be my study to preserve peace and to cultivate friendship on fair and honorable terms, and in the adjustment of any differences that may exist or arise to exhibit the forbearance becoming a powerful nation rather than the sensibility belonging to a gallant people."
    "In such measures as I may be called on to pursue in regard to the rights of the separate States I hope to be animated by a proper respect for those sovereign members of our Union, taking care not to confound the powers they have reserved to themselves with those they have granted to the Confederacy."
    "The management of the public revenue - that searching operation in all governments - is among the most delicate and important trusts in ours, and it will, of course, demand no inconsiderable share of my official solicitude. Under every aspect in which it can be considered it would appear that advantage must result from the observance of a strict and faithful economy. This I shall aim at the more anxiously both because it will facilitate the extinguishment of the national debt, the unnecessary duration of which is incompatible with real independence, and because it will counteract that tendency to public and private profligacy which a profuse expenditure of money by the Government is but too apt to engender. Powerful auxiliaries to the attainment of this desirable end are to be found in the regulations provided by the wisdom of Congress for the specific appropriation of public money and the prompt accountability of public officers."
    "With regard to a proper selection of the subjects of impost with a view to revenue, it would seem to me that the spirit of equity, caution, and compromise in which the Constitution was formed requires that the great interests of agriculture, commerce, and manufactures should be equally favored, and that perhaps the only exception to this rule should consist in the peculiar encouragement of any products of either of them that may be found essential to our national independence."
    "Internal improvement and the diffusion of knowledge, so far as they can be promoted by the constitutional acts of the Federal Government, are of high importance."
    "Considering standing armies as dangerous to free governments in time of peace, I shall not seek to enlarge our present establishment, nor disregard that salutary lesson of political experience which teaches that the military should be held subordinate to the civil power. The gradual increase of our Navy, whose flag has displayed in distant climes our skill in navigation and our fame in arms; the preservation of our forts, arsenals, and dockyards, and the introduction of progressive improvements in the discipline and science of both branches of our military service are so plainly prescribed by prudence that I should be excused for omitting their mention sooner than for enlarging on their importance. But the bulwark of our defense is the national militia, which in the present state of our intelligence and population must render us invincible. As long as our Government is administered for the good of the people, and is regulated by their will; as long as it secures to us the rights of person and of property, liberty of conscience and of the press, it will be worth defending; and so long as it is worth defending a patriotic militia will cover it with an impenetrable aegis. Partial injuries and occasional mortifications we may be subjected to, but a million of armed freemen, possessed of the means of war, can never be conquered by a foreign foe. To any just system, therefore, calculated to strengthen this natural safeguard of the country I shall cheerfully lend all the aid in my power."
    "It will be my sincere and constant desire to observe toward the Indian tribes within our limits a just and liberal policy, and to give that humane and considerate attention to their rights and their wants which is consistent with the habits of our Government and the feelings of our people."
    "The recent demonstration of public sentiment inscribes on the list of Executive duties, in characters too legible to be overlooked, the task of reform, which will require particularly the correction of those abuses that have brought the patronage of the Federal Government into conflict with the freedom of elections, and the counteraction of those causes which have disturbed the rightful course of appointment and have placed or continued power in unfaithful or incompetent hands."
    "In the performance of a task thus generally delineated I shall endeavor to select men whose diligence and talents will insure in their respective stations able and faithful cooperation, depending for the advancement of the public service more on the integrity and zeal of the public officers than on their numbers."
    "A diffidence, perhaps too just, in my own qualifications will teach me to look with reverence to the examples of public virtue left by my illustrious predecessors, and with veneration to the lights that flow from the mind that founded and the mind that reformed our system. The same diffidence induces me to hope for instruction and aid from the coordinate branches of the Government, and for the indulgence and support of my fellow-citizens generally. And a firm reliance on the goodness of that Power whose providence mercifully protected our national infancy, and has since upheld our liberties in various vicissitudes, encourages me to offer up my ardent supplications that He will continue to make our beloved country the object of His divine care and gracious benediction."

    ]
    Bush=["Vice President Cheney, Mr. Chief Justice, President Carter, President Bush, President Clinton, reverend clergy, distinguished guests, fellow citizens:"
    "On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country. I am grateful for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed."
    "At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century, America defended our own freedom by standing watch on distant borders. After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical —and then there came a day of fire."
    "We have seen our vulnerability —and we have seen its deepest source. For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed hatred and excuse murder — violence will gather, and multiply in destructive power, and cross the most defended borders, and raise a mortal threat. There is only one force of history that can break the reign of hatred and resentment, and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human freedom."
    "We are led, by events and common sense, to one conclusion: The survival of liberty in our land increasingly depends on the success of liberty in other lands. The best hope for peace in our world is the expansion of freedom in all the world."
    "America's vital interests and our deepest beliefs are now one. From the day of our Founding, we have proclaimed that every man and woman on this earth has rights, and dignity, and matchless value, because they bear the image of the Maker of Heaven and earth. Across the generations we have proclaimed the imperative of self-government, because no one is fit to be a master, and no one deserves to be a slave. Advancing these ideals is the mission that created our Nation. It is the honorable achievement of our fathers. Now it is the urgent requirement of our nation's security, and the calling of our time."
    "So it is the policy of the United States to seek and support the growth of democratic movements and institutions in every nation and culture, with the ultimate goal of ending tyranny in our world."
    "This is not primarily the task of arms, though we will defend ourselves and our friends by force of arms when necessary. Freedom, by its nature, must be chosen, and defended by citizens, and sustained by the rule of law and the protection of minorities. And when the soul of a nation finally speaks, the institutions that arise may reflect customs and traditions very different from our own. America will not impose our own style of government on the unwilling. Our goal instead is to help others find their own voice, attain their own freedom, and make their own way."
    "The great objective of ending tyranny is the concentrated work of generations. The difficulty of the task is no excuse for avoiding it. America's influence is not unlimited, but fortunately for the oppressed, America's influence is considerable, and we will use it confidently in freedom's cause."
    "My most solemn duty is to protect this nation and its people against further attacks and emerging threats. Some have unwisely chosen to test America's resolve, and have found it firm."
    "We will persistently clarify the choice before every ruler and every nation: The moral choice between oppression, which is always wrong, and freedom, which is eternally right. America will not pretend that jailed dissidents prefer their chains, or that women welcome humiliation and servitude, or that any human being aspires to live at the mercy of bullies."
    "We will encourage reform in other governments by making clear that success in our relations will require the decent treatment of their own people. America's belief in human dignity will guide our policies, yet rights must be more than the grudging concessions of dictators; they are secured by free dissent and the participation of the governed. In the long run, there is no justice without freedom, and there can be no human rights without human liberty."
    "Some, I know, have questioned the global appeal of liberty —though this time in history, four decades defined by the swiftest advance of freedom ever seen, is an odd time for doubt. Americans, of all people, should never be surprised by the power of our ideals. Eventually, the call of freedom comes to every mind and every soul. We do not accept the existence of permanent tyranny because we do not accept the possibility of permanent slavery. Liberty will come to those who love it."
    "Today, America speaks anew to the peoples of the world:"
    "All who live in tyranny and hopelessness can know: the United States will not ignore your oppression, or excuse your oppressors. When you stand for your liberty, we will stand with you."
    "Democratic reformers facing repression, prison, or exile can know: America sees you for who you are: the future leaders of your free country."
    "The rulers of outlaw regimes can know that we still believe as Abraham Lincoln did: Those who deny freedom to others deserve it not for themselves; and, under the rule of a just God, cannot long retain it."
    "The leaders of governments with long habits of control need to know: To serve your people you must learn to trust them. Start on this journey of progress and justice, and America will walk at your side."
    "And all the allies of the United States can know: we honor your friendship, we rely on your counsel, and we depend on your help. Division among free nations is a primary goal of freedom's enemies. The concerted effort of free nations to promote democracy is a prelude to our enemies' defeat."
    "Today, I also speak anew to my fellow citizens:"
    "From all of you, I have asked patience in the hard task of securing America, which you have granted in good measure. Our country has accepted obligations that are difficult to fulfill, and would be dishonorable to abandon. Yet because we have acted in the great liberating tradition of this nation, tens of millions have achieved their freedom. And as hope kindles hope, millions more will find it. By our efforts, we have lit a fire as well —a fire in the minds of men. It warms those who feel its power, it burns those who fight its progress, and one day this untamed fire of freedom will reach the darkest corners of our world."
    "A few Americans have accepted the hardest duties in this cause —in the quiet work of intelligence and diplomacy ... the idealistic work of helping raise up free governments ... the dangerous and necessary work of fighting our enemies. Some have shown their devotion to our country in deaths that honored their whole lives —and we will always honor their names and their sacrifice."
    "All Americans have witnessed this idealism, and some for the first time. I ask our youngest citizens to believe the evidence of your eyes. You have seen duty and allegiance in the determined faces of our soldiers. You have seen that life is fragile, and evil is real, and courage triumphs. Make the choice to serve in a cause larger than your wants, larger than yourself —and in your days you will add not just to the wealth of our country, but to its character."
    "America has need of idealism and courage, because we have essential work at home —the unfinished work of American freedom. In a world moving toward liberty, we are determined to show the meaning and promise of liberty."
    "In America's ideal of freedom, citizens find the dignity and security of economic independence, instead of laboring on the edge of subsistence. This is the broader definition of liberty that motivated the Homestead Act, the Social Security Act, and the G.I. Bill of Rights. And now we will extend this vision by reforming great institutions to serve the needs of our time. To give every American a stake in the promise and future of our country, we will bring the highest standards to our schools, and build an ownership society. We will widen the ownership of homes and businesses, retirement savings and health insurance —preparing our people for the challenges of life in a free society. By making every citizen an agent of his or her own destiny, we will give our fellow Americans greater freedom from want and fear, and make our society more prosperous and just and equal."
    "In America's ideal of freedom, the public interest depends on private character —on integrity, and tolerance toward others, and the rule of conscience in our own lives. Self-government relies, in the end, on the governing of the self. That edifice of character is built in families, supported by communities with standards, and sustained in our national life by the truths of Sinai, the Sermon on the Mount, the words of the Koran, and the varied faiths of our people. Americans move forward in every generation by reaffirming all that is good and true that came before —ideals of justice and conduct that are the same yesterday, today, and forever."
    "In America's ideal of freedom, the exercise of rights is ennobled by service, and mercy, and a heart for the weak. Liberty for all does not mean independence from one another. Our nation relies on men and women who look after a neighbor and surround the lost with love. Americans, at our best, value the life we see in one another, and must always remember that even the unwanted have worth. And our country must abandon all the habits of racism, because we cannot carry the message of freedom and the baggage of bigotry at the same time."
    "From the perspective of a single day, including this day of dedication, the issues and questions before our country are many. From the viewpoint of centuries, the questions that come to us are narrowed and few. Did our generation advance the cause of freedom? And did our character bring credit to that cause?"
    "These questions that judge us also unite us, because Americans of every party and background, Americans by choice and by birth, are bound to one another in the cause of freedom. We have known divisions, which must be healed to move forward in great purposes —and I will strive in good faith to heal them. Yet those divisions do not define America. We felt the unity and fellowship of our nation when freedom came under attack, and our response came like a single hand over a single heart. And we can feel that same unity and pride whenever America acts for good, and the victims of disaster are given hope, and the unjust encounter justice, and the captives are set free."
    "We go forward with complete confidence in the eventual triumph of freedom. Not because history runs on the wheels of inevitability; it is human choices that move events. Not because we consider ourselves a chosen nation; God moves and chooses as He wills. We have confidence because freedom is the permanent hope of mankind, the hunger in dark places, the longing of the soul. When our Founders declared a new order of the ages; when soldiers died in wave upon wave for a union based on liberty; when citizens marched in peaceful outrage under the banner Freedom Now —they were acting on an ancient hope that is meant to be fulfilled. History has an ebb and flow of justice, but history also has a visible direction, set by liberty and the Author of Liberty."
    "When the Declaration of Independence was first read in public and the Liberty Bell was sounded in celebration, a witness said, It rang as if it meant something. In our time it means something still. America, in this young century, proclaims liberty throughout all the world, and to all the inhabitants thereof. Renewed in our strength — tested, but not weary — we are ready for the greatest achievements in the history of freedom."
    "May God bless you, and may He watch over the United States of America."

    ]
    d=dict()
    for i in AndrewJackson[0].split():
            if i not in d:
                    d[i]=1
            else:
                    d[i]=d[i]+1
    d2=dict()

    for i in Bush[0].split():
            if i not in d2:
                    d2[i]=1
            else:
                    d2[i]=d2[i]+1

    sorted_d=sorted(d.items(), key=operator.itemgetter(1))
    sorted_d2=sorted(d2.items(), key=operator.itemgetter(1))
    print "AndrewJackson"
    print ""
    for i in range (len(d)-1,len(d)-11,-1):
        print sorted_d[i]
    print ""
    print "Bush"
    print ""
    for i in range (len(d2)-1,len(d2)-11,-1):
        print sorted_d2[i]
def survey():
    sur=list()
    sur=[["Division","Very Good","Good","Bad","Very bad"],["Class quality",13.1,37.1,8.7,1.5
        ],["Method",10.6,34.6,13.4,1.9],["Friendship",27.1,40.0,2.9,1.5],["Teacher",16.2,37.8,6.8,0.8],
       ["School facility",11.4,29.8,14.8,4.9],["School environment",12.2,26.5,14.9,4.4],
        ["Major",13.5,29.7,11.1,2.4],["School life",13.7,37.6,4.1,1.2]]
    sur2=sur[1:]
    sum=0
    for h in sur2:
        sum1=h[1]+h[2]
        sum+=sum1
    sum2=0
    for h in sur2:
        sum3=h[3]+h[4]
        sum2+=sum3
    good=sum/len(sur2)
    bad=sum2/len(sur2)
    
    print "Good average is "+str(good)
    print "Bad average is "+str(bad)
def lab11():
	speech()
	survey()
def main():
    lab11()
if __name__=="__main__": 
     main()
wn.exitonclick()