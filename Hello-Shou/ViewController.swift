//
//  ViewController.swift
//  Hello-Shou
//
//  Created by Wei Song on 4/7/16.
//  Copyright © 2016 Wei Song. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var shouLogo: UIImageView!
    
    var showIfTheShouLogoAppear:Bool = true
    
    @IBAction func clickMe(sender: UIButton) {
        if showIfTheShouLogoAppear{
            shouLogo.hidden = true
            showIfTheShouLogoAppear = false
        }else{
            shouLogo.hidden = false
            showIfTheShouLogoAppear = true
        }
        
    }

}

