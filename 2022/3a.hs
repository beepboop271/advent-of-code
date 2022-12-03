import Data.Char (isUpper, ord)
import Data.List (singleton)
import Data.Set (findMin, fromList, intersection)

priority :: Char -> Int
priority c
  | isUpper c = ord c - ord 'A' + 27
  | otherwise = ord c - ord 'a' + 1

findCommonChar :: String -> String -> Char
findCommonChar s1 s2 = findMin (intersection (fromList s1) (fromList s2))

process :: [(String, String)] -> Int
process = sum . map (priority . uncurry findCommonChar)

splitHalf :: String -> (String, String)
splitHalf s = splitAt (div (length s) 2) s

processInput :: [String] -> [String]
processInput = singleton . show . process . map splitHalf

main = interact (unlines . processInput . lines)
