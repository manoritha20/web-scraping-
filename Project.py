import { Component } from '@angular/core';

@Component({

selector: 'app-root',

templateUrl: './app.component.html',

styleUrls: ['./app.component.css']

})

export class AppComponent {

title = 'poc';

customerSelect: string = "No";

customers = ["Vikas", "Vinay", "bla bla"];

customerDeatils = [

{ name: "Vikas", AccountType: "Savings", Balance: "122435" },
{ name: "Vinay", AccountType: "Current", Balance: "2517471" },

{ name: "bla bla", AccountType: "Normal", Balance: "423523" }
];

showCustomerUI: any;

showTable: any;

showCustomerTable() {

this.showTable = "Yes";

for (var i = 0; i < this.customerDeatils.length; i++) {

  if (this.customerDeatils[i].name == this.customerSelect) {

    this.showCustomerUI = this.customerDeatils[i];

    break;

  }

}
}

}

Module.ts

import { BrowserModule } from '@angular/platform-browser';

import { NgModule } from '@angular/core';

import { FormsModule } from '@angular/forms';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';

@NgModule({

declarations: [

AppComponent
],

imports: [

BrowserModule,

FormsModule,

AppRoutingModule
],

providers: [],

bootstrap: [AppComponent]

})

export class AppModule { }
