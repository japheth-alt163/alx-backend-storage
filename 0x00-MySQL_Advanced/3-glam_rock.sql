-- List all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, 
       IFNULL(YEAR(2022) - SUBSTRING_INDEX(lifespan, '-', 1), 0) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
