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