import Data.List (sort, sortOn)
import Data.Ord ( Down(Down) )

answer :: [[Integer]] -> Integer
answer [] = 0
answer l = (sum . take 3 . sortOn Down . map sum) l

process :: [[Integer]] -> [Integer] -> [String] -> [String]
process elves elf [] = [show (answer elves)]
process elves elf ("":inp) = process (elf:elves) [] inp
process elves elf (val:inp) = process elves ((read val):elf) inp

main = interact (unlines . process [] [] . lines)
