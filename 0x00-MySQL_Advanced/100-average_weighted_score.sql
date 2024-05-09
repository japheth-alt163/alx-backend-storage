-- Create the stored procedure ComputeAverageWeightedScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_weight INT;
    DECLARE weighted_score FLOAT;

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
END//
DELIMITER ;
