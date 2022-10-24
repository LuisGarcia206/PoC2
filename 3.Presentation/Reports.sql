--1 obtain the weekly average number of trips for an area, defined by region.
SELECT q.region,
       COUNT(DISTINCT CONCAT(q.origin_coord,q.destination_coord)) / 
       MAX(COUNT(DISTINCT EXTRACT(WEEK FROM PARSE_DATE('%Y-%m-%d',SUBSTR(q.datetime,1,10))))) OVER (PARTITION BY REGION) avg_trips_week
  FROM db1_poc2.trips q
 GROUP BY q.region;

--2 From the two most commonly appearing regions, which is the latest datasource?
SELECT d.region,
       max(d.datetime) last_datetime_trip,
       max(d.datasource) last_datasource_trip
  FROM db1_poc2.trips d
  JOIN (SELECT w.region,
               w.last_datetime
          FROM (SELECT q.region,
                       RANK() OVER (ORDER BY COUNT(DISTINCT CONCAT(q.origin_coord,q.destination_coord)) DESC) rnk,
                       MAX(q.datetime) last_datetime
                   FROM db1_poc2.trips q
                 GROUP BY q.region) w
         WHERE w.rnk <=2) z
    ON z.region = d.region
   AND z.last_datetime = d.datetime
 GROUP BY d.region;

--3 What regions has the "cheap_mobile" datasource appeared in
SELECT d.region,
       max(d.datetime) last_datetime_trip,
       max(d.datasource) last_datasource_trip
  FROM db1_poc2.trips d
  JOIN (SELECT w.region,
               w.last_datetime
          FROM (SELECT q.region,
                       RANK() OVER (ORDER BY COUNT(DISTINCT CONCAT(q.origin_coord,q.destination_coord)) DESC) rnk,
                       MAX(q.datetime) last_datetime
                   FROM db1_poc2.trips q
                 GROUP BY q.region) w
         WHERE w.rnk <=2) z
    ON z.region = d.region
   AND z.last_datetime = d.datetime
 GROUP BY d.region
 HAVING max(d.datasource) = 'cheap_mobile';