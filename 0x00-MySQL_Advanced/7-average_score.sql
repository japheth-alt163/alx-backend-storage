-- Create the stored procedure ComputeAverageScoreForUser
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_projects INT;
    DECLARE average DECIMAL(10, 2);

    -- Calculate total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate total number of projects
    SELECT COUNT(DISTINCT project_id) INTO total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate average score
    IF total_projects > 0 THEN
        SET average = total_score / total_projects;
    ELSE
        SET average = 0;
    END IF;

    -- Update the average score for the user
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END //

DELIMITER ;
