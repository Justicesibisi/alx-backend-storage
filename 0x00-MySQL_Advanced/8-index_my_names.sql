-- An SQL Script that creates an index
-- on names names table and the first letter of the name.


CREATE INDEX idx_name_first ON
names(name(1));
