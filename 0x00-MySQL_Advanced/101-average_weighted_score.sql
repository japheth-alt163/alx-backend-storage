-- Create the stored procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_score FLOAT;
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    -- Open the cursor to iterate through all users
    OPEN cur;

    -- Loop through each user
    users_loop: LOOP
        FETCH cur INTO user_id;
        IF done THEN
            LEAVE users_loop;
        END IF;

        -- Reset variables for each user
        SET total_score = 0;
        SET total_weight = 0;

        -- Calculate the total weighted score for the user
        SELECT SUM(c.score * p.weight), SUM(p.weight)
        INTO total_score, total_weight
        FROM corrections c
        INNER JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the weighted average score
        IF total_weight > 0 THEN
            SET weighted_score = total_score / total_weight;
        ELSE
            SET weighted_score = 0;
        END IF;

        -- Update the users table with the computed average weighted score
        UPDATE users
        SET average_score = weighted_score
        WHERE id = user_id;
    END LOOP;

    -- Close the cursor
    CLOSE cur;
END//
DELIMITER ;
