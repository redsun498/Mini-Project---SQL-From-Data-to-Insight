SELECT
    COALESCE(adventure.`Release Year`, '') AS adventure_release_date,
    COALESCE(adventure.`Total Sales`, 0) AS adventure_total_sales,
    COALESCE(adventure.`Genre`, '') AS adventure_genre,
    COALESCE(non_adventure.`Release Year`, '') AS non_adventure_release_date,
    COALESCE(non_adventure.`Total Sales`, 0) AS non_adventure_total_sales,
    COALESCE(non_adventure.`Genre`, '') AS non_adventure_genre
FROM
    (SELECT `Release Year`, `Total Sales`, `Genre` FROM df1 WHERE `Genre` <> 'Adventure' LIMIT 10) AS non_adventure
CROSS JOIN
    (SELECT `Release Year`, `Total Sales`, `Genre` FROM df1 WHERE `Genre` = 'Adventure' LIMIT 10) AS adventure
ORDER BY 
    adventure.`Release Year` DESC,
    non_adventure.`Release Year` DESC,
    adventure.`Total Sales` DESC,
    non_adventure.`Total Sales` DESC;
    
    select * from df;