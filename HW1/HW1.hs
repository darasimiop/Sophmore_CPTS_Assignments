-- CptS 355 - Spring 2024 Assignment 1
-- Please include your name and the names of the students with whom you discussed
--any of the problems in this homework
-- Darasimi
module HW1
where
import Data.Char (toUpper)

-- Helper function to check if a character is lowercase
isLower :: Char -> Bool
isLower c = c >= 'a' && c <= 'z'

-- Helper function to check if an element is present in a list
contains :: Eq a => a -> [a] -> Bool
contains _ [] = False
contains val (x:xs)
    | val == x = True
    | otherwise = contains val xs

-- 1. exists
exists :: Eq t => t -> [t] -> Bool
exists _ [] = False
exists val (x:xs)
    | val == x = True
    | otherwise = exists val xs

-- 2. listUnion
listUnion :: Eq a => [a] -> [a] -> [a]
listUnion list1 list2 = removeDuplicates (list1 ++ list2)
    where
        -- Helper function to remove duplicates from a list
        removeDuplicates :: Eq a => [a] -> [a]
        removeDuplicates [] = []
        removeDuplicates (y:ys)
            | contains y ys = removeDuplicates ys
            | otherwise = y : removeDuplicates ys

-- 3. replace
replace :: (Eq t1, Num t1) => t1 -> t2 -> [t2] -> [t2]
replace _ _ [] = []
replace n v (x:xs)
    | n == 0 = v : xs
    | otherwise = x : replace (n - 1) v xs

-- 4. prereqFor
prereqFor :: Eq t => [(a, [t])] -> t -> [a]
prereqFor [] _ = []
prereqFor ((course, prerequisites):rest) targetCourse
    | contains targetCourse prerequisites = course : restResult
    | otherwise = restResult
    where
        restResult = prereqFor rest targetCourse

-- 5. isPalindrome
isPalindrome :: [Char] -> Bool
isPalindrome input = cleanInput == reverseString cleanInput
    where
        -- Helper function to clean the input
        cleanInput :: [Char]
        cleanInput = cleanString input

        -- Helper function to reverse a string
        reverseString :: [Char] -> [Char]
        reverseString [] = []
        reverseString (y:ys) = reverseString ys ++ [y]

        -- Helper function to clean the string
        cleanString :: [Char] -> [Char]
        cleanString [] = []
        cleanString (z:zs)
            | isAlphaNumeric z = toUpperAscii z : cleanString zs
            | otherwise = cleanString zs

        -- Helper function to check if a character is alphanumeric
        isAlphaNumeric :: Char -> Bool
        isAlphaNumeric c = isLetter c || isDigit c

        -- Helper function to check if a character is a letter
        isLetter :: Char -> Bool
        isLetter c = c >= 'A' && c <= 'Z' || c >= 'a' && c <= 'z'

        -- Helper function to check if a character is a digit
        isDigit :: Char -> Bool
        isDigit c = c >= '0' && c <= '9'

        -- Helper function to convert a character to uppercase
        toUpperAscii :: Char -> Char
        toUpperAscii c
            | isLower c = toEnum (fromEnum c - fromEnum 'a' + fromEnum 'A')
            | otherwise = c

-- 6. groupSumtoN
groupSumtoN :: (Ord a, Num a) => a -> [a] -> [[a]]
groupSumtoN _ [] = [[]]
groupSumtoN n lst = helper n lst []
    where
        helper :: (Ord a, Num a) => a -> [a] -> [[a]] -> [[a]]
        helper _ [] acc = reverse acc
        helper limit (x:xs) acc
            | x > limit = helper limit xs ([reverse [x]] ++ acc)
            | otherwise = case acc of
                            [] -> helper limit xs [[x]]
                            (ys:rest) -> if sumList ys + x <= limit
                                            then helper limit xs ((x:ys):rest)
                                            else helper limit xs (reverse (x:ys):acc)

        -- Helper function to calculate the sum of a list
        sumList :: Num b => [b] -> b
        sumList [] = 0
        sumList (z:zs) = z + sumList zs
