podatki = readtable('Kiti.csv','ReadVariableNames',false);
podatki = table2array(podatki);

%%%%%%%
% a)
% narisemo histogram za dane podatke
n = length(podatki);
k_1 = quantile(podatki, 0.25);
k_3 = quantile(podatki, 0.75);
l = 2 * (k_3 - k_1) / n^(1/3)

i = 0;
razredi = [0];
while i < max(podatki)
    i = i + 0.1; % l~0.1
    razredi = [razredi i];
end
figure(1)
histogram(podatki,razredi);


%%%%%%%
% b)
% ocenimo parametra alfa in lambda za gama
% porazdelitev z metodo momentov
mi_1 = sum(podatki) / n;
mi_2 = sum(podatki .^ 2) / n;

alfa_m = mi_1^2 / (mi_2 - mi_1^2);
lambda_m = mi_1 / (mi_2 - mi_1^2);


%%%%%%%
% c)
% ocenimo parametra alfa in lambda za gama
% porazdelitev z metodo najvecjega verjetja
lambda = @(alfa) n * alfa / sum(podatki);
dl_alfa = @(alfa) n*log(lambda(alfa)) + sum(log(podatki)) - n*psi(alfa);

alfa_v = fzero(dl_alfa, 1)
lambda_v = lambda(alfa_v)


%%%%%%%
% d)
% dorisemo dobljeni porazdelitvi na histogram
gama = @(x,lambda,alfa) lambda.^alfa .* x.^(alfa-1) .* exp(-x.*lambda) ./ gamma(alfa);

figure(2)
hold on
histogram(podatki,razredi,'Normalization','pdf');
x = 0:0.01:5;
y_m = gama(x,lambda_m,alfa_m);
y_v = gama(x,lambda_v,alfa_v);
plot(x,y_m)
plot(x,y_v)
hold off

%%%%%%%
% e)
% histogram in porazdelitvi narisemo na logaritemski lestvici
m = max(podatki) / l; % število razredov
x_log = logspace(-1,1,m);

figure(3)
hold on
histogram(podatki,x_log,'Normalization','pdf');
set(gca,'xscale','log');
y_m_log = gama(x_log,lambda_m,alfa_m);
y_v_log = gama(x_log,lambda_v,alfa_v);
plot(x_log, y_m_log)
plot(x_log, y_v_log)
hold off

