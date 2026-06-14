{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Banco de Dados\
\
## Tecnologia Utilizada\
Supabase PostgreSQL\
\
## Objetivo\
Persistir dados financeiros em nuvem para atender aos requisitos da entrega final.\
\
## Tabela transactions\
Campos:\
id\
tipo\
valor\
categoria\
descricao\
data\
\
## Processo de Sincroniza\'e7\'e3o\
O usu\'e1rio registra transa\'e7\'f5es localmente.\
Os dados s\'e3o armazenados em JSON.\
O comando fintrack sync \'e9 executado.\
Os registros s\'e3o enviados ao Supabase.\
Os dados ficam persistidos em PostgreSQL.}