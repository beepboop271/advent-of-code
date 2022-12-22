import Data.Set (Set, empty, insert, size)
import Text.Printf (printf)

type Point = (Int, Int)
type Rope = [Point]
type Visited = Set Point

distSquared :: Point -> Point -> Int
distSquared (x1, y1) (x2, y2) = (x2 - x1)^2 + (y2 - y1)^2

findStep :: Point -> Point -> Point
findStep head@(hx, hy) next@(nx, ny)
  | distSquared head next <= 2 = (0, 0)
  | dx == 0          = (0, stepY)
  | dy == 0          = (stepX, 0)
  | abs dx == 1      = (dx, stepY)
  | abs dy == 1      = (stepX, dy)
  | abs dx == abs dy = (stepX, stepY)
  | otherwise        = error (show dx ++ " " ++ show dy)
  where
    stepX = quot dx (abs dx)
    stepY = quot dy (abs dy)
    dx = hx - nx
    dy = hy - ny

stepSingle :: Visited -> Rope -> Point -> (Rope, Visited)
stepSingle v rope (0, 0) = (rope, v)
stepSingle v ((hx, hy):rest) (dx, dy) = case rest of
  []     -> ([head'], insert head' v)
  next:_ -> let (rest', v') = stepSingle v rest (findStep head' next)
            in (head':rest', v')
  where
    head' = (hx+dx, hy+dy)

stepN :: Int -> Visited -> Rope -> Point -> (Rope, Visited)
stepN 0 v r _ = (r, v)
stepN n v r p = stepN (n-1) v' r' p
  where
    (r', v') = stepSingle v r p

stepAll :: Visited -> Rope -> [(Int, Int, Int)] -> Visited
stepAll v r [] = v
stepAll v r ((dx, dy, amount):rest) = stepAll v' r' rest
  where
    (r', v') = stepN amount v r (dx, dy)

parse :: String -> (Int, Int, Int)
parse (d:' ':num) = case d of
  'L' -> (-1, 0, amount)
  'R' -> (1, 0, amount)
  'U' -> (0, 1, amount)
  'D' -> (0, -1, amount)
  where
    amount = read num
parse _ = error ""

processInput :: Int -> [String] -> String
processInput n = show
  . size
  . stepAll (insert (0, 0) empty) (replicate n (0, 0))
  . map parse

main = interact (
    (\ inp -> printf "A: %s\nB: %s\n" (processInput 2 inp) (processInput 10 inp))
    . lines
  )
