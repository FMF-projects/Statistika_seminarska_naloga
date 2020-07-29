podatki = readtable('TempPulz.csv');
% temperatura, spol, pulz
moski = table2array(podatki(1:65,:));
zenske = table2array(podatki(66:130,:));

%%%%%%%
% a)
% ocenimo povprecja in standardne odklone
temp_m = mean(moski(:,1));
temp_z = mean(zenske(:,1));
pulz_m = mean(moski(:,3));
pulz_z = mean(zenske(:,3));

odklon_temp_m = sqrt(sum((moski(:,1) - temp_m).^2) /65);
odklon_temp_z = sqrt(sum((zenske(:,1) - temp_z).^2) /65);
odklon_pulz_m = sqrt(sum((moski(:,3) - pulz_m).^2) /65);
odklon_pulz_z = sqrt(sum((zenske(:,3) - pulz_z).^2) /65);

%%%%%%%
% b)
% za povprecja dolocimo 95% intervale zaupanja
z_alfa = 1.96;
int_temp_m = [temp_m - odklon_temp_m * z_alfa, temp_m + odklon_temp_m * z_alfa];
int_temp_z = [temp_z - odklon_temp_z * z_alfa, temp_z + odklon_temp_z * z_alfa];
int_pulz_m = [pulz_m - odklon_pulz_m * z_alfa, pulz_m + odklon_pulz_m * z_alfa];
int_pulz_z = [pulz_z - odklon_pulz_z * z_alfa, pulz_z + odklon_pulz_z * z_alfa];

