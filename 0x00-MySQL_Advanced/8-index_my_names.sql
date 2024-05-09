-- Create the index idx_name_first
CREATE INDEX idx_name_first ON names (LEFT(name, 1));
