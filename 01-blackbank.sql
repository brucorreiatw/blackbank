CREATE DATABASE blackbank;

\c blackbank;

CREATE TABLE "Debits" (
    "debtId" VARCHAR(100) NOT NULL,
    "name" VARCHAR(100) NOT NULL,
    "governmentId" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    "debtAmount" VARCHAR(100) NOT NULL,
    "debtDueDate" VARCHAR(100) NOT NULL,
    UNIQUE ("debtId")
);

CREATE TABLE "Credits" (
    "debtId" VARCHAR(100) NOT NULL,
    "paidAt" VARCHAR(100) NOT NULL,
    "paidAmount" VARCHAR(100) NOT NULL,
    "paidBy" VARCHAR(100) NOT NULL,
    UNIQUE ("debtId")
);