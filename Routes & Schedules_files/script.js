var _____WB$wombat$assign$function_____ = function(name) {return (self._wb_wombat && self._wb_wombat.local_init && self._wb_wombat.local_init(name)) || self[name]; };
if (!self.__WB_pmw) { self.__WB_pmw = function(obj) { this.__WB_source = obj; return this; } }
{
  let window = _____WB$wombat$assign$function_____("window");
  let self = _____WB$wombat$assign$function_____("self");
  let document = _____WB$wombat$assign$function_____("document");
  let location = _____WB$wombat$assign$function_____("location");
  let top = _____WB$wombat$assign$function_____("top");
  let parent = _____WB$wombat$assign$function_____("parent");
  let frames = _____WB$wombat$assign$function_____("frames");
  let opener = _____WB$wombat$assign$function_____("opener");

/**
 * @version     $Id$
 * @author      JoomlaUX!
 * @package     Joomla.Site
 * @subpackage  mod_jux_megamenu
 * @copyright   Copyright (C) 20013 - 2015 by JoomlaUX. All rights reserved.
 * @license     http://www.gnu.org/licenses/gpl.html GNU/GPL version 3
*/



!function($){   
    $(document).ready(function(){    
        function jux_sticky () {
            if(window.innerWidth > 1024){
                 $window = $(window);      
                    var lastpos     = $(window).scrollTop(),
                        mainnav     = $('#js-mainnav'),
                        header      = $('header');
                    if(mainnav.length){  
                        elmHeightMainnav = mainnav.outerHeight(true);
                        elmHeightHeader  = header.outerHeight(true);
                        elmHeight        = elmHeightHeader + elmHeightMainnav; 
                        $(window).scroll(function() {   
                            if(window.innerWidth > 1024){
                                var scrolltop = $(window).scrollTop();
                                if(lastpos > elmHeight){
                                    if(!mainnav.hasClass('affix')) {
                                        mainnav.addClass('affix');    
                                    }
                                } else if(scrolltop <= elmHeight) {
                                    mainnav.removeClass('affix');
                                }
                                lastpos = scrolltop;
                           }else{
                                $('#js-mainnav').removeClass('affix');
                           }
                        });  
                }
                new Headroom(document.querySelector("#js-mainnav"), {
                    tolerance: 10,
                    offset : 205,
                    classes: {
                      initial: "animated"
                    }
                }).init();
            }else{
                $('#js-mainnav').removeClass('affix');
            }
        }
        jux_sticky();
        $(window).resize( function(){
            jux_sticky();
        });
    });

}(jQuery);


}
/*
     FILE ARCHIVED ON 04:35:57 Dec 02, 2024 AND RETRIEVED FROM THE
     INTERNET ARCHIVE ON 20:45:10 Dec 08, 2024.
     JAVASCRIPT APPENDED BY WAYBACK MACHINE, COPYRIGHT INTERNET ARCHIVE.

     ALL OTHER CONTENT MAY ALSO BE PROTECTED BY COPYRIGHT (17 U.S.C.
     SECTION 108(a)(3)).
*/
/*
playback timings (ms):
  captures_list: 0.638
  exclusion.robots: 0.023
  exclusion.robots.policy: 0.01
  esindex: 0.012
  cdx.remote: 6.036
  LoadShardBlock: 60.916 (3)
  PetaboxLoader3.datanode: 104.089 (5)
  load_resource: 442.773 (2)
  PetaboxLoader3.resolve: 325.533 (2)
*/