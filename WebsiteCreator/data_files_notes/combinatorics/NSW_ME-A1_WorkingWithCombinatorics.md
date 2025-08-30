###   Concepts 

 - arrangements
 - fundamental counting principle, also known as the multiplication principle
 - pigeonhole principle
 - generalised pigeonhole principle
 - ordered selections
 - unordered selections
 - factorial
 - permutations
 - combinations
 - binomial expansion
 - Pascal's triangle and binomial coefficients
 - Pascal's triangle identity


###   Notes 

 - $ n!$ is the number of ways of selecting n objects with no replacement or repetition.  Order is important.

 - Permutations = ordered

 - $^nP_r$ is the number of ways of making an ordered selection or r objects from a total of n objects.

 - Combinations = unordered.  Given the order is not important, therefore will be a smaller number than the equivalent permutation.

 - $^nC_r = (^n_r)$ is the number of ways of making an unordered selection or r objects from a total of n objects.

 - When calculating how many ways items can be arranged in a circle e.g. table, necklace:
    * questions assume position of items in a circle is irrelevant
    * item appearing at the top of the circle vs the bottom of the circle is the same thing for example
    * Therefore n items can be arranged around a circle in (n-1)! ways, as the positioning of the first item is irrelevant

 - When x items in an arrangement need to be together / consecutive, treat these as one item, and make the corresponding reduction to n.
     * For example when 5 different colour balls need to be arranged but red and yellow need to be next to each other than the number of arrangements is 4! treating the red and yellow as one.
     * But these x objects can be arranged in x! ways, in above case 2!
    * Therefore total arrangements  = 4! x 2!

 - Be on the lookout for the options in the "other" part of the arrangement.
    * For example if questions asks how many ways can 3 people sit next to each other at a round table of 7 people:
    * The 3 people can sit next to each other in 3! ways  - where they sit on round table is irrelevant
    * Don’t forget that the other 4 people can sit next to each other in 4! different ways
    * Therefore 3! x 4!

 - Each item in Pascals triangle can be written as $^{\text{row index}}C_{\text{column index}}$ where both the indices start from zero.
 
 - To satisfy oneself as to workings of binomial expansion it can be quickly tested with something simple like $(a+b)^2$


