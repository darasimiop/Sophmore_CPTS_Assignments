-- CptS 355 - Spring 2024 Assignment 2
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework

module HW2
     where

data Tree a = LEAF a | NODE a (Tree a) (Tree a)
              deriving (Show, Read, Eq)


{- 1-  merge2 & merge2Tail & mergeN - 22% -}
--merge2
merge2 :: Ord a => [a] -> [a] -> [a]
merge2 [] ys = ys
merge2 xs [] = xs
merge2 (x:xs) (y:ys)
    | x <= y    = x : merge2 xs (y:ys)
    | otherwise = y : merge2 (x:xs) ys

--merge2Tail
merge2Tail :: Ord a => [a] -> [a] -> [a]
merge2Tail xs [] = xs
merge2Tail [] ys = ys
merge2Tail xs@(x:xs') ys@(y:ys')
    | x <= y    = x : merge2Tail xs' ys
    | otherwise = y : merge2Tail xs ys'


--mergeN
mergeN :: (Foldable t, Ord a) => t [a] -> [a]
mergeN = foldr merge2 []

{- 2 - getInRange & countInRange - 18% -}

--getInRange
getInRange :: Ord a => a -> a -> [a] -> [a]
getInRange v1 v2 = filter (\x -> v1 < x && x < v2)

--countInRange
countInRange :: Ord a => a -> a -> [[a]] -> Int
countInRange v1 v2 = length . concatMap (filter (\x -> v1 < x && x < v2))



{- 3 -  addLengths & addAllLengths - 18% -}

data LengthUnit =  INCH  Int | FOOT  Int | YARD  Int
                   deriving (Show, Read, Eq)
-- addLengths
addLengths :: LengthUnit -> LengthUnit -> LengthUnit
addLengths (INCH i1) (INCH i2) = INCH (i1 + i2)
addLengths (FOOT f1) (FOOT f2) = INCH (12 * (f1 + f2))
addLengths (YARD y1) (YARD y2) = INCH (36 * (y1 + y2))
addLengths (INCH i) (FOOT f) = INCH (i + 12 * f)
addLengths (FOOT f) (INCH i) = INCH (i + 12 * f)
addLengths (INCH i) (YARD y) = INCH (i + 36 * y)
addLengths (YARD y) (INCH i) = INCH (i + 36 * y)
addLengths (FOOT f) (YARD y) = INCH (12 * f + 36 * y)
addLengths (YARD y) (FOOT f) = INCH (12 * f + 36 * y)
-- addAllLengths
addAllLengths :: [[LengthUnit]] -> LengthUnit
addAllLengths = INCH . sum . map (sum . map convert)
    where
        convert (INCH i) = i
        convert (FOOT f) = 12 * f
        convert (YARD y) = 36 * y

{-4 - sumTree and createSumTree - 22%-}
-- sumTree
sumTree :: Num p => Tree p -> p
sumTree (LEAF x) = x
sumTree (NODE _ left right) = sumTree left + sumTree right

-- createSumTree
createSumTree :: Num a => Tree a -> Tree a
createSumTree (LEAF x) = LEAF x
createSumTree (NODE x left right) = NODE (sumTree (NODE x left right)) (createSumTree left) (createSumTree right)

instance Functor Tree where
    fmap f (LEAF x) = LEAF (f x)
    fmap f (NODE x left right) = NODE (f x) (fmap f left) (fmap f right)


{-5 - foldListTree - 20%-}
data ListTree a = ListLEAF [a] | ListNODE [(ListTree a)]
                  deriving (Show, Read, Eq)
foldListTree :: (a -> b -> b) -> b -> ListTree a -> b
foldListTree f base (ListLEAF xs) = foldr f base xs
foldListTree f base (ListNODE ts) = foldr (\tree acc -> foldListTree f acc tree) base ts



{- 6- Create two tree values :  Tree Integer  and  listTree a ;  Both trees should have at least 3 levels. -}
-- Tree Integer
myTree :: Tree Integer
myTree = NODE 1
         (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6))
         (NODE 7 (LEAF 8) (LEAF 9))

-- ListTree a
l1 :: ListTree String
l1 = ListLEAF ["School","-","of","-","Electrical"]

l2 :: ListTree String
l2 = ListLEAF ["-","Engineering","-"]

l3 :: ListTree String
l3 = ListLEAF ["and","-","Computer","-"]

l4 :: ListTree String
l4 = ListLEAF ["Science"]

l5 :: ListTree String
l5 = ListLEAF ["-WSU"]

n1 :: ListTree String
n1 = ListNODE [l1,l2]

n2 :: ListTree String
n2 = ListNODE [n1,l3]

t5 :: ListTree String
t5 = ListNODE [n2,l4,l5]
