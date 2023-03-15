#!/bin/bash
echo "Ingrese el nombre del empleado"
read nombre
echo "Ingrese la cantidad de horas trabajadas"
read cantHoras
echo "Ingrese el valor de la hora trabajada"
read vlrHora
bonificacion=0
porcentaje1=0.05
porcentaje2=0.10
porcentajeTotal=0.08
subtotal=`expr $cantHoras * $vlrHora`
subtotal=`expr $subtotal * $porcentajeSalud`
neto=0

if [ $cantHoras -lt 20 ]
then
	echo "Usted trabajo menos de 20 horas"
	bonificacion=`expr $subtotal*$porcentaje1`
elif [ $cantHoras -ge 20 ]
then
	echo "Usted trabajo igual o mas de 20 horas"
	bonificacion=`expr $subtotal*$porcentaje2`
else
	echo "Error"
fi

neto=`expr $subtotal + $bonificacion`
echo "Salario basico = $subtotal"
echo "Deducción por salud y pension = $porcentajeTotal"
echo "Bonificación = $bonificacion"
echo "Salario Neto = $neto"
