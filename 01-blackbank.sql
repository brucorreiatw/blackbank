CREATE DATABASE blackbank;

\c blackbank;

CREATE TABLE "Debits" (
    "debtId" int NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "governmentId" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    "debtAmount" float NOT NULL,
    "debtDueDate" date NOT NULL,
    UNIQUE ("debtId")
);

CREATE TABLE "Credits" (
    "debtId" int NOT NULL,
    "paidAt" TIMESTAMP NOT NULL,
    "paidAmount" float NOT NULL,
    "paidBy" VARCHAR(100) NOT NULL,
    UNIQUE ("debtId")
);