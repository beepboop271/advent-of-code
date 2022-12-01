answer :: [[Integer]] -> Integer
answer [] = 0
answer l = (maximum . map sum) l

process :: [[Integer]] -> [Integer] -> [String] -> [String]
process elves elf [] = [show (answer elves)]
process elves elf ("":inp) = process (elf:elves) [] inp
process elves elf (val:inp) = process elves (read val:elf) inp

main = interact (unlines . process [] [] . lines)
