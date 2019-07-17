CREATE DATABASE dashboard_info;
use dashboard_info;

CREATE TABLE emailer_info (
  id int(10) unsigned NOT NULL AUTO_INCREMENT,
  to_addr VARCHAR(255),
  subject VARCHAR(255),
  from_addr VARCHAR(255),
  password VARCHAR(255),
  dd_public_dashboard_url VARCHAR(255),
  PRIMARY KEY(id)
);

INSERT INTO emailer_info
  (to_addr, subject, from_addr, password, dd_public_dashboard_url)
VALUES
  ('test@test.com', 'testing ', 'tester@tester.com', 'm8ff', 'www.google.com');