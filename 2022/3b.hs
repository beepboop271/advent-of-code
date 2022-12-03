import Data.Char (isUpper, ord)
import Data.List (singleton)
import Data.Set (findMin, fromList, intersection)

priority :: Char -> Int
priority c
  | isUpper c = ord c - ord 'A' + 27
  | otherwise = ord c - ord 'a' + 1

findCommonPriority :: String -> String -> String -> Int
findCommonPriority s1 s2 s3 = (priority . findMin)
  (intersection (intersection (fromList s1) (fromList s2)) (fromList s3))

processInput :: Int -> [String] -> [String]
processInput acc (s1:s2:s3:rest) =
  processInput (acc + findCommonPriority s1 s2 s3) rest
processInput acc _ = [show acc]

main = interact (unlines . processInput 0 . lines)
